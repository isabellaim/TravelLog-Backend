from django.db import models
from django.contrib.auth.models import User
from trips.models import TravelEntry

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    entry = models.ForeignKey(TravelEntry, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'entry') #esto es para evitar duplicados

    def __str__(self):
        return f"{self.user.username} guardó {self.entry.destination_name}"