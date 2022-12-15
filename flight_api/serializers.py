from rest_framework import serializers
from .models import Flight, Seats



"""Register serializers"""

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class SeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = '__all__'