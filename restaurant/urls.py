from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu-items/', views.MenuItemsView.as_view(), name="menu-items"),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name="menu_item"),
    path('api-token-auth/', obtain_auth_token),
    # path('book/', views.book, name="book"),
    # path('reservations/', views.reservations, name="reservations"),
    # path('bookings', views.bookings, name='bookings'),
]