from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    
    filter_backends = [DjangoFilterBackend,  # edited
                       filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['flight__number', 'origin', 'destination']
    ordering_fields = ['flight_number', 'date_reserved','origin', 'destination']
    filterset_fields = {
        'flight_number': ['exact']     
    }
    

class SeatMapViewSet(viewsets.ModelViewSet):
    queryset = SeatMap.objects.all()
    serializer_class = SeatMapSerializer
    

@api_view(['GET'])
def hello(request):
    if request.method=='GET':
        return Response({"FlightNumber": 123})



@api_view(['GET'])
def model_flight(request):
    if request.method=='GET':
        queryset = Flight.objects.all()
        response = FlightSerializer(queryset, many=True)
        return Response(response.data)


@api_view(['GET'])
def model_seat(request):
    if request.method=='GET':
        queryset = SeatMap.objects.all()
        response = SeatMapSerializer(queryset, many=True)
        return Response(response.data)
