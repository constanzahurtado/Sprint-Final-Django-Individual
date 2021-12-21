from django.contrib.auth import get_user_model
from django.contrib import admin
from django.db.models import fields
from .models import Receta, Ingrediente, Contacto

admin.site.register(Contacto)

User = get_user_model()

class IngredienteInline(admin.StackedInline):
    model = Ingrediente
    extra = 0
    fields = ['nombre_ingrediente', 'cantidad', 'calorias', 'azucares', 'sodio', 'grasas' ]

class RecetaUsuario(admin.ModelAdmin):
    inlines =[IngredienteInline]
    list_display = ['nombre_receta','usuario']
    raw_id_fields = ['usuario']


admin.site.register(Receta, RecetaUsuario)