from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Trip, TravelEntry
from .serializers import (
    CategorySerializer, 
    TripSerializer, 
    TripListSerializer,
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
        # Solo mostrar los viajes del usuario autenticado
        return Trip.objects.filter(user=self.request.user).prefetch_related('entries')
    
    def get_serializer_class(self):
        # Usar serializer ligero para listados
        if self.action == 'list':
            return TripListSerializer
        return TripSerializer
    
    def perform_create(self, serializer):
        # Asignar automáticamente el usuario autenticado
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['get'])
    def entries(self, request, pk=None):
        """Endpoint para obtener solo las entradas de un viaje específico"""
        trip = self.get_object()
        entries = trip.entries.all()
        serializer = TravelEntrySerializer(entries, many=True)
        return Response(serializer.data)


class TravelEntryViewSet(viewsets.ModelViewSet):
    serializer_class = TravelEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Solo entradas de viajes del usuario autenticado
        return TravelEntry.objects.filter(
            trip__user=self.request.user
        ).select_related('trip', 'category')
    
    def perform_create(self, serializer):
        # Verificar que el trip pertenece al usuario
        trip = serializer.validated_data['trip']
        if trip.user != self.request.user:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("No puedes agregar entradas a este viaje")
        serializer.save()

