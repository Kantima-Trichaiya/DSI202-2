from django import forms
from .models import Rental

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = []  # No fields needed; user, equipment, and start_time are set programmatically