from django.contrib import admin
from .models import Trip, TravelEntry

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['title', 'description']
    date_hierarchy = 'created_at'

@admin.register(TravelEntry)
class TravelEntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'destination_name', 'trip', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['destination_name', 'review']
    date_hierarchy = 'created_at'
    date_hierarchy = 'created_at'
