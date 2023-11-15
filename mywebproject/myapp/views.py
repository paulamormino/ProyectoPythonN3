from django.shortcuts import render, redirect
from .models import Producto, Cliente
from .forms import ProductoForm, ClienteForm, BusquedaForm

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listar_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/crear_producto.html', {'form': form})

def inicio(request):
    return render(request, 'inicio.html')
