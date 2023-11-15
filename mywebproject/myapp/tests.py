from django.test import TestCase
from django.urls import reverse
from .models import Producto, Cliente
from .forms import ProductoForm, ClienteForm, BusquedaForm
from .views import listar_productos, crear_producto, inicio

class ProductoTestCase(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(nombre="Ejemplo", precio=10.0)

    def test_listar_productos_view(self):
        response = self.client.get(reverse('listar_productos'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['productos'], ['<Producto: Ejemplo>'])

    def test_crear_producto_view(self):
        form_data = {'nombre': 'Nuevo Producto', 'precio': 20.0}
        form = ProductoForm(data=form_data)
        self.assertTrue(form.is_valid())

class ClienteTestCase(TestCase):
    def test_crear_cliente(self):
        cliente = Cliente.objects.create(nombre="Cliente Ejemplo", email="cliente@example.com")
        self.assertIsNotNone(cliente)

class FormsTestCase(TestCase):
    def test_producto_form(self):
        form_data = {'nombre': 'Nuevo Producto', 'precio': 20.0}
        form = ProductoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_cliente_form(self):
        form_data = {'nombre': 'Nuevo Cliente', 'email': 'cliente@example.com'}
        form = ClienteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_busqueda_form(self):
        form_data = {'busqueda': 'ejemplo'}
        form = BusquedaForm(data=form_data)
        self.assertTrue(form.is_valid())
