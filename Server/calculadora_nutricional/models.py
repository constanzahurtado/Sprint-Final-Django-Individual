from django.db import models
from django.db.models.deletion import SET_NULL
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

CHOICES=[('Usuario','Usuario'),
         ('Administrador','Administrador')]

class Usuario(models.Model):
    user_name = models.CharField(max_length= 50)
    email_address = models.CharField(max_length= 30)
    password = models.CharField(max_length= 12)
    nombre_grupo_usuario = models.CharField(max_length=20, choices=CHOICES)
    last_login = models.CharField(max_length= 300)

class Contacto(models.Model):
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length= 50)
    email = models.CharField(max_length= 30)
    mensaje = models.TextField(max_length= 600)

class Comentario(models.Model):
    nombre_comentario = models.CharField(max_length= 50)
    comentario = models.TextField(max_length= 800)

# class Receta(models.Model):
#     titulo = models.CharField(max_length= 50)
#     porcion_habitual = models.FloatField()
#     fecha_creacion = models.DateField(("Fecha"), default=date.today)

# class Ingrediente(models.Model):
#     receta = models.ForeignKey(Receta, null = True, on_delete=SET_NULL)
#     nombre_ingrediente = models.CharField(max_length= 50)
#     cantidad_ingrediente= models.FloatField()
#     calorias = models.FloatField()
#     azucares = models.FloatField()
#     grasas = models.FloatField()
#     sodio = models.FloatField()
