from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signupuser, name='signupuser'),
    path('logout',views.logoutuser, name='logoutuser'),
    path('login',views.loginuser, name='loginuser'),
    path('create', views.createtodos, name = 'createtodos'),
    path('currenttodos', views.currenttodos, name = 'currenttodos'),
    path('completedtodos', views.completedtodos, name = 'completedtodos'),
    path('todo/<int:todo_pk>', views.viewtodo, name = 'viewtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name = 'completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name = 'deletetodo'),



]