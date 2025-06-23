from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.MenuItemsView.as_view(), name="menu"),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name="menu_item"),
    # path('book/', views.book, name="book"),
    # path('reservations/', views.reservations, name="reservations"),
    # path('bookings', views.bookings, name='bookings'),
]