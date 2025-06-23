# from django.http import HttpResponse
import json
from datetime import datetime
from .forms import BookingForm
from .models import MenuItem, Booking
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from .serializers import MenuItemSerializer, BookingSerializer

# Create your views here.
class bookingview(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data)

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# def reservations(request):
#     date = request.GET.get('date',datetime.today().date())
#     bookings = Booking.objects.all()
#     booking_json = serializers.serialize('json', bookings)
#     return render(request, 'bookings.html',{"bookings":booking_json})

# def book(request):
#     form = BookingForm()
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {'form':form}
#     return render(request, 'book.html', context)

# def menu(request):
#     menu_data = Menu.objects.all()
#     main_data = {"menu": menu_data}
#     return render(request, 'menu.html', {"menu": main_data})

# def display_menu_item(request, pk=None):
#     if pk:
#         menu_item = Menu.objects.get(pk=pk)
#     else:
#         menu_item = ""
#     return render(request, 'menu_item.html', {"menu_item": menu_item})

# @csrf_exempt
# def bookings(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)

#         exist = Booking.objects.filter(
#             reservation_date=data['reservation_date'],
#             reservation_slot=data['reservation_slot']
#         ).exists()

#         if not exist:
#             booking = Booking(
#                 first_name=data['first_name'],
#                 reservation_date=data['reservation_date'],
#                 reservation_slot=data['reservation_slot']
#             )
#             booking.save()
#         else:
#             return HttpResponse("{\"error\":1}", content_type='application/json')

#     date_str = request.GET.get('date')
#     if date_str:
#         try:
#             date = datetime.strptime(date_str, '%Y-%m-%d').date()
#         except ValueError:
#             return HttpResponse('{"error": "Invalid date format"}', content_type='application/json', status=400)
#     else:
#         date = datetime.today().date()
#     bookings = Booking.objects.filter(reservation_date=date)
#     booking_json = serializers.serialize('json', bookings)
#     return HttpResponse(booking_json, content_type='application/json')