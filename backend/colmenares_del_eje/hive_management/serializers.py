from rest_framework import serializers  
from .models import Beehive

# Create your serializers here.

class beehive_serializer_input(serializers.ModelSerializer):
    class Meta:
        model = Beehive
        fields = [
            'location',
            'open_brood_frames',
            'capped_brood_frames',
            'queen_presence',
            'queen_color',
            'origin',
            'food_frames',
            'observations',
            'qr_code',
            'id_weather_conditions',
            'status'
        ]

class beehive_serializer_output(serializers.ModelSerializer):
    class Meta:
        model = Beehive
        fields = [
            'id',
            'registration_date',
            'location',
            'open_brood_frames',
            'capped_brood_frames',
            'queen_presence',
            'queen_color',
            'origin',
            'food_frames',
            'observations',
            'qr_code',
            'id_weather_conditions',
            'status'
        ]
