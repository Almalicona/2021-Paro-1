from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from Models.Tienda.forms import FormularioProducto, FormularioMarca, FormularioCategoria
from Models.Tienda.models import Producto, Marca, Categoria


class FormularioProductoView(HttpRequest):
    def registrar_producto(request):
        producto = FormularioProducto()
        return render(request, "crear_producto", {"form":producto})

    def procesar_producto(request):
        producto = FormularioProducto(request.POST)
        if producto.is_valid():
            producto.save()
            producto = FormularioProducto

        return render(request, "crear_producto.html", {"form":producto, "mensaje": 'OK'})

    def listar_productos(request):
        productos = Producto.objects.all()
        return render(request, "mostrar_productos.html",{"productos": productos})


class FormularioMarcaView(HttpRequest):
    def registrar_marca(request):
        marca = FormularioMarca()
        return render(request, "crear_marca.html", {"form":marca})

    def procesar_marca(request):
        marca = FormularioMarca(request.POST)
        if marca.is_valid():
            marca.save()
            marca = FormularioMarca

        return render(request, "crear_marca.html", {"form":marca, "mensaje": 'OK'})

    def listar_marca(request):
        marcas = Marca.objects.all()
        return render(request, "mostrar_marcas.html",{"marcas": marcas })

class FormularioCategoriaView(HttpRequest):
    def registrar_categoria(request):
        categoria = FormularioCategoria()
        return render(request, "crear_categoria.html", {"form":categoria})

    def procesar_categoria(request):
        categoria = FormularioCategoria(request.POST)
        if categoria.is_valid():
            categoria.save()
            categoria=FormularioCategoria

        return render(request,"crear_categoria.html", {"form":categoria, "mensaje": 'OK'})

    def listar_categorias(request):
        categorias = Categoria.objects.all()
        return render(request, "mostrar_categorias.html",{"categorias": categorias})
