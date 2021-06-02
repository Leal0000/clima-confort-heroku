from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import tipo_poliza, registro
from django.contrib import messages
from django.contrib.auth import login,  authenticate
import datetime
from datetime import date

# Create your views here.
@login_required




def table(request):
    tipo=tipo_poliza.objects.all()
    tabla= registro.objects.all()
    fecha_actual=datetime.datetime.now()
    variables ={
        'tabla' : tabla,
        'tipo' : tipo,
        'actual' : fecha_actual,
    }
    if request.POST:
        Registro = registro()
        Registro.nombre = request.POST.get('name')
        Registro.clave_nueva = request.POST.get('clave')
        tipo = tipo_poliza()
        tipo.id = int(request.POST.get('tipo'))
        Registro.tipo = tipo
        Registro.fecha = request.POST.get('fecha')
        f = request.POST.get('fecha')
        fa = datetime.datetime.strptime(f, "%Y-%m-%d")
        fe= fa + datetime.timedelta(days=90)
        Registro.fecha_termino = fe
        Registro.telefono = request.POST.get('telefono')
        Registro.email = request.POST.get('email')
        Registro.documento = request.FILES.get('documento')
        Registro.save()
        
    
    return render(request, "table/table.html", variables)

def formulario(request):

    tipo=tipo_poliza.objects.all()
    variables ={
        'tipo' : tipo
    }

    if request.POST:
        Registro = registro()
        Registro.nombre = request.POST.get('name')
        Registro.clave_nueva = request.POST.get('clave')
        tipo = tipo_poliza()
        tipo.id = int(request.POST.get('tipo'))
        Registro.tipo = tipo
        Registro.fecha = request.POST.get('fecha')
        Registro.telefono = request.POST.get('telefono')
        Registro.email = request.POST.get('email')
        Registro.documento = request.FILES.get('documento')
        Registro.save()

        
    
    return render(request, "table/formulario.html", variables)
     

def eliminar(request, id):

    registro1 = registro.objects.get(id=id)

    try:
        registro1.delete()
        mensaje = "Se ha eliminado el registro"
        messages.success(request, mensaje)
    except:
        mensaje="No se ha podido eliminar "
        messages.error(request, mensaje)
    
    return redirect('Table')

def actualizar(request, id):
    #Buscamos el registro
    registro1=registro.objects.get(id=id)
    tipo=tipo_poliza.objects.all()
    variables ={
        'registro' : registro1, 
        'tipo' : tipo
    }


    if request.POST:
        Registro = registro()
        Registro.id = request.POST.get('id')
        Registro.nombre = request.POST.get('name')
        Registro.clave_nueva = request.POST.get('clave')
        tipo = tipo_poliza()
        tipo.id = int(request.POST.get('tipo'))
        Registro.tipo = tipo
        Registro.fecha = request.POST.get('fecha')
        Registro.telefono = request.POST.get('telefono')
        Registro.email = request.POST.get('email')
        Registro.documento = request.FILES.get('documento')
        Registro.updated = registro1.created()
        Registro.save()

        try:
            registro1.delete()
            mensaje = "Se ha actulizado el registro"
            messages.success(request, mensaje)
        except:
            mensaje="No se ha podido actualizar "
            messages.error(request, mensaje)
        return redirect('Table')
    


    return render(request, "table/actualizar.html", variables)

    

