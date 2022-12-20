from django.db import models
from django.conf import settings

class Flight(models.Model):
    """To define a flight object """
    flight_number = models.CharField(max_length=50, blank=True,unique=True)
    date_reserved = models.DateTimeField(blank=True, null=True)
    origin = models.CharField(max_length=50, blank=True, null=True)
    destination = models.CharField(max_length=50, blank=True)
    capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.flight_number


class SeatMap(models.Model):
    """To define a seat object """
    seat_id = models.CharField(max_length=10, blank=True)
    available = models.BooleanField(default=True)
    UserProfile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flight = models.ForeignKey('flight_api.Flight', on_delete=models.CASCADE)
    date_reserved = models.DateTimeField(verbose_name='Reserved date',blank=True, null=True)
    destination = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.seat_id
    