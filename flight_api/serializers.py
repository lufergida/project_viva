from rest_framework import serializers
from .models import *



"""Register serializers"""

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class SeatMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatMap
        fields = '__all__'