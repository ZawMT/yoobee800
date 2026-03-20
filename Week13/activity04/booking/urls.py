from django.urls import path
from . import views

urlpatterns = [
    path('', views.makebooking, name='makebooking'),
    path('bookinginfo/', views.bookinginfo, name='bookinginfo'),
    path('api/slots/', views.api_slots, name='api_slots'),
    path('api/book/', views.api_book, name='api_book'),
]
