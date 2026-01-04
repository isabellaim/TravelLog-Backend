from rest_framework import serializers
from .models import Wishlist
from trips.models import TravelEntry


class WishlistSerializer(serializers.ModelSerializer):
    entry_id = serializers.PrimaryKeyRelatedField(
        queryset=TravelEntry.objects.all(),
        source='entry',
        write_only=True
    )
    
    class Meta:
        model = Wishlist
        fields = ['id', 'entry_id', 'added_at']
        read_only_fields = ['added_at']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
