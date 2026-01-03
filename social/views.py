from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Wishlist
from .serializers import WishlistSerializer


class WishlistViewSet(viewsets.ModelViewSet):
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Solo wishlist del usuario autenticado
        return Wishlist.objects.filter(user=self.request.user).select_related('entry', 'entry__trip')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=False, methods=['post'])
    def toggle(self, request):
        """Agregar o quitar de wishlist"""
        entry_id = request.data.get('entry_id')
        
        if not entry_id:
            return Response(
                {'error': 'Se requiere entry_id'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            wishlist_item = Wishlist.objects.get(user=request.user, entry_id=entry_id)
            wishlist_item.delete()
            return Response(
                {'message': 'Eliminado de wishlist', 'in_wishlist': False},
                status=status.HTTP_200_OK
            )
        except Wishlist.DoesNotExist:
            wishlist_item = Wishlist.objects.create(user=request.user, entry_id=entry_id)
            serializer = self.get_serializer(wishlist_item)
            return Response(
                {'message': 'Agregado a wishlist', 'in_wishlist': True, 'data': serializer.data},
                status=status.HTTP_201_CREATED
            )
    
    @action(detail=False, methods=['get'])
    def check(self, request):
        """Verificar si una entrada está en wishlist"""
        entry_id = request.query_params.get('entry_id')
        
        if not entry_id:
            return Response(
                {'error': 'Se requiere entry_id'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        exists = Wishlist.objects.filter(user=request.user, entry_id=entry_id).exists()
        return Response({'in_wishlist': exists})

