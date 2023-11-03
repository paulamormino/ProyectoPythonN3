from django.urls import path
from . import views

urlpatterns = [
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
]
