from rest_framework import serializers
from .models import Wishlist
from trips.serializers import TravelEntrySerializer


class WishlistSerializer(serializers.ModelSerializer):
    entry = TravelEntrySerializer(read_only=True)
    entry_id = serializers.PrimaryKeyRelatedField(
        queryset=Wishlist.objects.all(),
        source='entry',
        write_only=True
    )
    
    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'entry', 'entry_id', 'added_at']
        read_only_fields = ['user', 'added_at']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
