# /myproject/myapp/urls.py
from django.urls import path
from .views import home, EquipmentListView, EquipmentDetailView, RentalCreateView, EquipmentListCreateAPIView, EquipmentRetrieveUpdateAPIView

urlpatterns = [
    path('', home, name='home'),  # Home page at root URL
    path('equipments/', EquipmentListView.as_view(), name='equipment_list'),
    path('equipments/<int:pk>/', EquipmentDetailView.as_view(), name='equipment_detail'),
    path('equipments/<int:pk>/rent/', RentalCreateView.as_view(), name='rental_create'),
    path('api/equipments/', EquipmentListCreateAPIView.as_view(), name='equipment_list_create_api'),
    path('api/equipments/<int:pk>/', EquipmentRetrieveUpdateAPIView.as_view(), name='equipment_retrieve_update_api'),
]