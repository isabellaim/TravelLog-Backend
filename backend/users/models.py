from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # aqui lo relacione el perfil con el usuario de Django
    foto_perfil_url = models.URLField(max_length=500, blank=True, null=True)
    biografia = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"