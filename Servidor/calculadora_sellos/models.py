from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.conf import settings
from django.urls import reverse


CHOICES=[('Usuario','Usuario'),
         ('Pyme','Pyme')]

class Usuario(models.Model):
    user_name = models.CharField(max_length= 50)
    email_address = models.CharField(max_length= 30)
    password = models.CharField(max_length= 12)
    nombre_grupo_usuario = models.CharField(max_length=20, choices=CHOICES)
    last_login = models.CharField(max_length= 300)


class Receta(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=CASCADE)
    nombre_receta = models.CharField(max_length= 30)
    porcion = models.FloatField()
    fecha = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("calculadora_sellos:detalle_receta", kwargs={"id":self.id})
    
    def get_editar_url(self):
        return reverse("calculadora_sellos:editar", kwargs={"id":self.id})

    def get_ingrediente_hijos(self):
        return self.ingrediente_set.all()

class Ingrediente(models.Model):
    receta = models.ForeignKey(Receta, on_delete=CASCADE)
    nombre_ingrediente = models.CharField(max_length= 30)
    cantidad = models.FloatField()
    calorias = models.FloatField()
    azucares = models.FloatField()
    sodio = models.FloatField()
    grasas = models.FloatField()

    totalCalorias = models.FloatField()
    totalAzucares = models.FloatField()
    totalSodio = models.FloatField()
    totalGrasas= models.FloatField()

    def calculate_total(self):
        return self.calorias*self.cantidad/100

    def calculate_total2(self):
        return self.azucares*self.cantidad/100
    
    def calculate_total3(self):
        return self.sodio*self.cantidad/100
    
    def calculate_total4(self):
        return self.grasas*self.cantidad/100
          
    def save(self, *args, **kwargs):
        self.totalCalorias=self.calculate_total()
        self.totalAzucares=self.calculate_total2()
        self.totalSodio=self.calculate_total3()
        self.totalGrasas=self.calculate_total4()
        super().save(*args, **kwargs)


    # def azucaresIngrediente(self):
    #     return self.azucares*self.cantidad/100

    # def save_azucares(self, *args, **kwargs):
    #     self.totalAzucares=self.azucaresIngrediente()
    #     super().save(*args, **kwargs)


 
    def get_absolute_url(self):
        return reverse("calculadora_nutricional:detalle", kwargs={"id":self.id})

 
class Contacto(models.Model):
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length= 50)
    email = models.CharField(max_length= 30)
    mensaje = models.TextField(max_length= 600)


