from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signupuser, name='signupuser'),
    path('logout',views.logoutuser, name='logoutuser'),
    path('login',views.loginuser, name='loginuser'),

    path('currenttodos', views.currenttodos, name = 'currenttodos'),
]