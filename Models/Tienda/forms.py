from django import forms

from Models.Tienda.models import Categoria, Marca, Producto


class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class FormularioMarca(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'})}

