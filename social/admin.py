from django.contrib import admin
from .models import Wishlist

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'entry', 'added_at']
    list_filter = ['added_at']
    search_fields = ['user__username', 'entry__destination_name']
    date_hierarchy = 'added_at'
    list_select_related = ['user', 'entry']
