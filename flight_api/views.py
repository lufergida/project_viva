from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

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
