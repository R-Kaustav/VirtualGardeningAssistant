from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomePage, name='WelcomePage'),
    path('user/', views.userprojecthomepage, name='UserProjectHomePage'),
    path('project/', views.projecthomepage, name='projecthomepage'),
    path('login/', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('login_logic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('register/', views.UserRegisterPageCall, name='UserRegisterPageCall'),
    path('register_logic/', views.UserRegisterLogic, name='UserRegisterLogic'),
]
