from django.contrib import admin
from django.urls import path
from userlogin import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.userLogin, name='login'),
    path('logout', views.userLogout, name='logout')
]
