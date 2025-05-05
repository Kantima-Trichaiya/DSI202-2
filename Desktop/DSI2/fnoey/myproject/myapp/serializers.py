from rest_framework import serializers
from .models import Equipment

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'name', 'is_available', 'rental_price', 'description', 'image']
        read_only_fields = ['id']  # Prevent updating the ID