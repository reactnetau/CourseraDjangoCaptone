from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('restaurant.urls')),
    path('api/api-token-auth/', obtain_auth_token),
    path('api/restaurant/booking/', include(router.urls)), 
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]