from django import forms
from .models import Receta, Ingrediente, Contacto, Usuario


class UsuariosForm(forms.ModelForm):
   class Meta:
        model = Usuario
        fields = ('user_name','email_address', 'password', 'nombre_grupo_usuario')

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ('nombre_receta', 'porcion')

class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ('nombre_ingrediente', 'cantidad', 'calorias', 'azucares', 'sodio', 'grasas')

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ('nombre','apellido','email', 'mensaje')

