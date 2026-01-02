from django.contrib import admin
from .models import Category, Trip, TravelEntry

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['title', 'description']
    date_hierarchy = 'created_at'

@admin.register(TravelEntry)
class TravelEntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'destination_name', 'trip', 'category', 'rating', 'created_at']
    list_filter = ['category', 'rating', 'created_at']
    search_fields = ['destination_name', 'review']
    date_hierarchy = 'created_at'
