from django.urls import path
from . import views

urlpatterns = [
    path('gardenplanning/', views.gardenplanning, name='gardenplanning'),
]