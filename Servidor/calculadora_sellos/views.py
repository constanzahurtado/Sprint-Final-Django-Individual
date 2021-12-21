from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404
from .models import Receta, Ingrediente
from.forms import RecetaForm, IngredienteForm, ContactoForm, UsuariosForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout
from django.forms.models import modelformset_factory
from django.contrib.auth.models import User, Group
from django.db.models import Avg, Max, Min, Sum



def index(request):
    return render(request,'calculadora_sellos/index.html')

def resultado(request):
    return render(request,'calculadora_sellos/resultado.html')

def recursos_externos(request):
    return render(request,'calculadora_sellos/recursos_externos.html')

def sobre_pagina(request):
    return render(request,'calculadora_sellos/sobre_pagina.html')

def preguntas_frecuentes(request):
    return render(request,'calculadora_sellos/preguntas_frecuentes.html')

def registro(request):
    if request.method == "POST":
        form=UsuariosForm(data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["user_name"]
            email_address = form.cleaned_data["email_address"]
            password=form.cleaned_data["password"]
            usuario = form.save(commit = False)
            usuario.save()
            
            user_group = User.objects.create_user(user_name, email_address,password)
            user_group.save()
            
            grupo = Group.objects.get(name=request.POST.get("nombre_grupo_usuario"))
            user_group.groups.add(grupo)
            return redirect('/ingreso_usuario')
    else:
        form = UsuariosForm()
        return render(request,'calculadora_sellos/registro_usuario.html',{'form': form})


def ingreso_usuario(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data =request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
        return redirect('/lista_recetas')
    else:
        form = AuthenticationForm()
        return render(request,'calculadora_sellos/ingreso_usuario.html', {"form":form})


@login_required(login_url = '/')
def lista_recetas(request, id=None):
    qs = Receta.objects.filter(usuario=request.user)
    context = {
        "lista":qs
    }
    return render(request, 'calculadora_sellos/lista_recetas.html', context)

    
@login_required(login_url = '/')
def detalle_receta(request, id=None):
    objeto = get_object_or_404(Receta, id=id, usuario=request.user)

    suma_cantidad = Ingrediente.objects.values('receta_id').annotate(Sum('cantidad'))
    suma_calorias = Ingrediente.objects.values('receta_id').annotate(Sum('totalCalorias'))
    suma_azucares = Ingrediente.objects.values('receta_id').annotate(Sum('totalAzucares'))
    suma_grasas = Ingrediente.objects.values('receta_id').annotate(Sum('totalGrasas'))
    suma_sodio = Ingrediente.objects.values('receta_id').annotate(Sum('totalSodio'))
        
    cantidad =([d["cantidad__sum"] for d in suma_cantidad if "cantidad__sum" in d][0])

    valor_cal =([d["totalCalorias__sum"] for d in suma_calorias if "totalCalorias__sum" in d][0])
    total_calorias = valor_cal*100/cantidad

    valor_azu =([d["totalAzucares__sum"] for d in suma_azucares if "totalAzucares__sum" in d][0])
    total_azucares = valor_azu*100/cantidad

    valor_gra =([d["totalGrasas__sum"] for d in suma_grasas if "totalGrasas__sum" in d][0])
    total_grasas = valor_gra*100/cantidad

    valor_so =([d["totalSodio__sum"] for d in suma_sodio if "totalSodio__sum" in d][0])
    total_sodio = valor_so*100/cantidad

    print(suma_grasas)

    
    context = {
        "detalle":objeto,
        "total_calorias": total_calorias,
        "total_azucares": total_azucares,
        "total_grasas": total_grasas,
        "total_sodio": total_sodio,

    }

    return render(request, 'calculadora_sellos/detalle_recetas.html', context)
  
@login_required(login_url = '/')
def crear_receta(request):
    form = RecetaForm(request.POST or None)
    ingredienteFormset= modelformset_factory(Ingrediente, form = IngredienteForm, extra = 0)
    formset = ingredienteFormset(request.POST or None)

    context = {
        "form":form,
        "formset":formset
    }
    if all([form.is_valid(), formset.is_valid()]):
        obj = form.save(commit=False)
        obj.usuario = request.user
        obj.save()
        for form in formset:
            child = form.save(commit = False)
            child.receta = obj
            child.save()
        formset.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'calculadora_sellos/crear_recetas.html', context)


@login_required(login_url = '/')
def editar_receta(request, id=None):
    objeto = get_object_or_404(Receta, id=id, usuario=request.user)
    form = RecetaForm(request.POST or None, instance= objeto)
    ingredienteFormset= modelformset_factory(Ingrediente, form = IngredienteForm, extra = 0)
    qs = objeto.ingrediente_set.all()
    formset = ingredienteFormset(request.POST or None, queryset=qs)
    context = {
        "form": form,
        "formset": formset,
        "objeto": objeto
    }
    if all([form.is_valid(), formset.is_valid()]):
        parent = form.save(commit = False)
        parent.save()
        for form in formset:
            child = form.save(commit = False)
            child.receta = parent
            child.save()
        context['mensaje'] = 'Los datos han sido guardados'
    return render(request, 'calculadora_sellos/crear-editar.html', context )

def cerrar_sesion(request):
    logout(request)
    return redirect('/ingreso_usuario')

def envio_mensaje(request):
    if request.method == "POST":
        form = ContactoForm(data = request.POST)
        if form.is_valid():
            contacto = form.save(commit = False)
            contacto.save()
        return redirect('/')
    else:
        form = ContactoForm()
        return render(request,'calculadora_sellos/contacto.html', {"form":form})    
   
def eliminar_receta(request, id):
    receta = Receta.objects.get(pk=id)
    receta.delete()
    return redirect('/lista_recetas')

