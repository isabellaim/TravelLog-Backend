from rest_framework import serializers
from .models import Trip, TravelEntry
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class TravelEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelEntry
        fields = [
            'id', 'trip', 'destination_name', 
            'review', 'rating', 'foto_url', 'created_at'
        ]
        read_only_fields = ['created_at']


class TripSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Trip
        fields = ['id', 'user', 'title', 'description', 'created_at']
        read_only_fields = ['created_at', 'user']
