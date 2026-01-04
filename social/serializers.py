from rest_framework import serializers
from .models import Wishlist
from trips.models import TravelEntry
from trips.serializers import TravelEntrySerializer


class WishlistSerializer(serializers.ModelSerializer):
    entry_id = serializers.PrimaryKeyRelatedField(
        queryset=TravelEntry.objects.all(),
        source='entry',
        write_only=True
    )
    entry = TravelEntrySerializer(read_only=True)
    
    class Meta:
        model = Wishlist
        fields = ['id', 'entry_id', 'entry', 'added_at']
        read_only_fields = ['added_at']
