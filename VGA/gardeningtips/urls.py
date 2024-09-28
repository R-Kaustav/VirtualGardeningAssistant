from django.urls import path
from . import views

urlpatterns = [
    path('gardentips/', views.gardeningtips, name='gardeningtips'),
]