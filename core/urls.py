"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from trips.views import TripViewSet, TravelEntryViewSet, public_trips_list
from users.views import ProfileViewSet, register, login, logout, user_detail
from social.views import WishlistViewSet

# Router para los ViewSets
router = DefaultRouter()
router.register(r'trips', TripViewSet, basename='trip')
router.register(r'entries', TravelEntryViewSet, basename='entry')
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'wishlist', WishlistViewSet, basename='wishlist')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API endpoints
    path('api/', include(router.urls)),
    
    # Public API (sin autenticación) - Para sustentación
    path('api/public/trips/', public_trips_list, name='public-trips'),
    
    # Auth endpoints
    path('api/auth/register/', register, name='register'),
    path('api/auth/login/', login, name='login'),
    path('api/auth/logout/', logout, name='logout'),
    path('api/auth/user/', user_detail, name='user-detail'),
]

