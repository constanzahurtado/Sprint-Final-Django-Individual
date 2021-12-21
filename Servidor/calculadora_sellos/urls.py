from django.urls import path
from .import views

app_name = 'calculadora_sellos'

urlpatterns = [
    path("",views.index, name ='index'),
    path('recursos_externos/', views.recursos_externos, name='recursos_externos'),
    path('sobre_pagina/', views.sobre_pagina, name='sobre_pagina'),
    path('preguntas_frecuentes/', views.preguntas_frecuentes, name='preguntas_frecuentes'),
    path('contacto/', views.envio_mensaje, name='contacto'),
    path('ingreso_usuario/', views.ingreso_usuario, name= 'ingreso_usuario'),
    path("lista_recetas",views.lista_recetas, name = 'lista'),
    path('<int:id>/',views.detalle_receta, name = 'detalle_receta'),
    path("<int:id>/editar",views.editar_receta, name = 'editar'),
    path('cerrar_sesion/',views.cerrar_sesion),
    path('registro', views.registro, name='registro'),
    path('resultado', views.resultado),
    path('<int:id>/eliminar',views.eliminar_receta),
    path("crear_receta",views.crear_receta, name = 'crear'),


]
