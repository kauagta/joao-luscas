
from django.contrib import admin
from django.urls import path
from kauacosta import views

urlpatterns = [
    path('',views.home,name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('usuario/', views.usuario, name='listagem_usuario'),

]
