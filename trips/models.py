from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TravelEntry(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='entries')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    destination_name = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.IntegerField(default=5) # Escala 1-5
    foto_url = models.URLField(max_length=500, blank=True, null=True)
    
    # Coordenadas para Google Maps / React Native Maps
    # Usamos DecimalField para máxima precisión geográfica
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.destination_name} ({self.trip.title})"