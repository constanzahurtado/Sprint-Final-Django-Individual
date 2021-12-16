from django.contrib import admin
from .models import Comentario, Contacto, Usuario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Contacto)
admin.site.register(Comentario)
