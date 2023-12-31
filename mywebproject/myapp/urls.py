from django.urls import path, include
from . import views

urlpatterns = [
    path('listar_productos/', views.listar_productos, name='listar_productos'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('', views.inicio, name='inicio'),
    path("", include("myapp.urls")),
]
