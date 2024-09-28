from django.urls import path
from . import views

urlpatterns = [
    path('taskreminder/', views.taskreminder, name='taskreminder'),
]