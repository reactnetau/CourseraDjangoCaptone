#define URL route for index() view
from django.urls import path
from .views import MenuItemsView, SingleMenuItemView, BookingViewSet

urlpatterns = [
    path('items/', MenuItemsView.as_view()),
    path('items/<int:pk>', SingleMenuItemView.as_view())
]
