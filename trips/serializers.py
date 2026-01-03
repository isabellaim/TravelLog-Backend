from rest_framework import serializers
from .models import Category, Trip, TravelEntry
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class TravelEntrySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), 
        source='category', 
        write_only=True
    )
    
    class Meta:
        model = TravelEntry
        fields = [
            'id', 'trip', 'category', 'category_id', 'destination_name', 
            'review', 'rating', 'foto_url', 'latitude', 'longitude', 'created_at'
        ]
        read_only_fields = ['created_at']


class TripSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    entries = TravelEntrySerializer(many=True, read_only=True)
    entries_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Trip
        fields = ['id', 'user', 'title', 'description', 'created_at', 'entries', 'entries_count']
        read_only_fields = ['created_at', 'user']
    
    def get_entries_count(self, obj):
        return obj.entries.count()


class TripListSerializer(serializers.ModelSerializer):
    """Versión ligera para listados sin incluir todas las entries"""
    user = UserSerializer(read_only=True)
    entries_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Trip
        fields = ['id', 'user', 'title', 'description', 'created_at', 'entries_count']
        read_only_fields = ['created_at', 'user']
    
    def get_entries_count(self, obj):
        return obj.entries.count()
