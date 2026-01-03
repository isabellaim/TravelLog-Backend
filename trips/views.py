from rest_framework import viewsets, permissions
from .models import Category, Trip, TravelEntry
from .serializers import (
    CategorySerializer, 
    TripSerializer, 
    TravelEntrySerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TripViewSet(viewsets.ModelViewSet):
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Trip.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TravelEntryViewSet(viewsets.ModelViewSet):
    serializer_class = TravelEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return TravelEntry.objects.filter(trip__user=self.request.user)

