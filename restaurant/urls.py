#define URL route for index() view
from django.urls import path
from .views import MenuItemsView, SingleMenuItemView, BookingViewSet, msg
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('restaurant/menu-items/', MenuItemsView.as_view()),
    path('restaurant/menu-items/<int:pk>', SingleMenuItemView.as_view()),
    path('message/', msg),

]
