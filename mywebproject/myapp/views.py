from django.shortcuts import render, redirect
from django.http import HttpResponseServerError
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import ProductoForm

def listar_productos(request):
    try:
        productos = Producto.objects.all()
        return render(request, 'productos/listar_productos.html', {'productos': productos})
    except Exception as e:
        return HttpResponseServerError("Error al obtener los productos: {}".format(e))

@login_required(login_url='/accounts/login/')
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
