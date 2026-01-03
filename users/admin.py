from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'biografia']
    search_fields = ['user__username', 'biografia']
    list_select_related = ['user']
