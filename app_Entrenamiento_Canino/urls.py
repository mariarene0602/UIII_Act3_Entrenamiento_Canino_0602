from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_entrenamiento_canino, name='inicio'),
    path('agregar-cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('ver-cliente/', views.ver_cliente, name='ver_cliente'),
    path('actualizar-cliente/<int:id_cliente>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('realizar-actualizacion-cliente/<int:id_cliente>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('borrar-cliente/<int:id_cliente>/', views.borrar_cliente, name='borrar_cliente'),
]