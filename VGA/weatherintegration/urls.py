from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.weatherintegration, name='weatherintegration'),
]