from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Equipment, Rental
from django.db.models import Q  # For complex queries
from .forms import RentalForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from rest_framework import generics
from .serializers import EquipmentSerializer


# Home Page (FBV)
def home(request):
    return render(request, 'myapp/home.html')

#  (CBV)
class EquipmentListView(ListView):
    model = Equipment
    template_name = 'myapp/equipment_list.html'
    context_object_name = 'equipments'  # Name of the variable in the template

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-rental_price')  # Get the default queryset
        query = self.request.GET.get('q')  # Get the search term from the URL (e.g., ?q=mountain)
        if query:
            # Filter where name or description contains the query (case-insensitive)
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        return queryset

#(CBV: DetailView)
class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = 'myapp/equipment_detail.html'
    context_object_name = 'equipment'  # Name of the variable in the template

class RentalCreateView(LoginRequiredMixin, CreateView):
    model = Rental
    form_class = RentalForm
    template_name = 'myapp/rental_form.html'

    def get_success_url(self):
        return reverse('equipment_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipment'] = Equipment.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        equipment = Equipment.objects.get(pk=self.kwargs['pk'])
        if not equipment.is_available:
            form.add_error(None, "This product is currently unavailable.")
            return self.form_invalid(form)
        form.save(user=self.request.user, equipment=equipment)
        return super().form_valid(form)
    
class EquipmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class EquipmentRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer