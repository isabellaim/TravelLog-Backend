from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Trip, TravelEntry
from .serializers import (
    TripSerializer, 
    TravelEntrySerializer
)


class TripViewSet(viewsets.ModelViewSet):
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Por defecto retorna solo los viajes del usuario
        return Trip.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=False, methods=['get'])
    def all(self, request):
        """GET /api/trips/all/ - Obtener todos los viajes de todos los usuarios"""
        trips = Trip.objects.all().order_by('-created_at')
        serializer = self.get_serializer(trips, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def my_trips(self, request):
        """GET /api/trips/my_trips/ - Obtener solo los viajes del usuario autenticado"""
        trips = Trip.objects.filter(user=request.user).order_by('-created_at')
        serializer = self.get_serializer(trips, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def entries(self, request, pk=None):
        """GET /api/trips/{id}/entries/ - Obtener todas las entradas de un trip específico"""
        trip = self.get_object()
        entries = TravelEntry.objects.filter(trip=trip).order_by('-created_at')
        serializer = TravelEntrySerializer(entries, many=True)
        return Response(serializer.data)


class TravelEntryViewSet(viewsets.ModelViewSet):
    """
    ViewSet para crear, editar y eliminar entradas.
    Para LEER entradas, usar: GET /api/trips/{id}/entries/
    """
    serializer_class = TravelEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Solo para operaciones de escritura (PUT, PATCH, DELETE)
        return TravelEntry.objects.filter(trip__user=self.request.user)

