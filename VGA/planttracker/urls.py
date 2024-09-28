from django.urls import path
from . import views

urlpatterns = [
    path('plantracker/', views.planttracker, name='planttracker'),
]