from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup',views.signupuser, name='signupuser'),
    path('currenttodos', views.currenttodos, name = 'currenttodos'),
]