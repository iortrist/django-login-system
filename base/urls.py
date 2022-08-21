from django.urls import path
from base import views

urlpatterns = [
    path('register/', views.userRegister, name='register'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),

    path('', views.home, name='home'),
]
