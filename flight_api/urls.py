from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = []

urlpatterns += [
    path('hello/', views.hello),
    path('flightObjects/', views.model_flight),
    path('seatObjects/', views.model_seat),
]

