from core.forms import obraForm
from core.models import Obra
from django.shortcuts import render, redirect

# Create your views here.

def home (request):
    return render(request, 'core/index.html')

def nosotros (request):
    return render(request, 'core/contactanos.html')
    
def inicio (request):
    return render(request, 'core/inicio.html')

def artistas (request):
    return render(request, 'core/paginaartistas.html')

def tipo (request):
    return render(request, 'core/paginatipoarte.html')

def anonimo (request):
    return render(request, 'core/anonimo.html')

def informacion1 (request):
    return render(request, 'core/informacion1.html')

def informacion2 (request):
    return render(request, 'core/informacion2.html')

def informacion3 (request):
    return render(request, 'core/informacion3.html')

def deartistas (request):
    return render(request, 'core/paginadeartistas.html')

def subir (request):
    return render(request, 'core/subir.html')

def formulario (request):
    return render(request, 'core/formulario.html')

def registro (request):
    return render(request, 'core/registrarse.html')

def principal (request):
    return render(request, 'core/principal2.html')

def leonardo (request):
    return render(request, 'core/paginaleonardo.html')

def escultura (request):
    return render(request, 'core/paginaescultura.html')

def pensador (request):
    return render(request, 'core/pensador.html')

def discobolo (request):
    return render(request, 'core/discobolo.html')

def venus (request):
    return render(request, 'core/venus.html')

def monalisa (request):
    return render(request, 'core/paginalamonalisa.html')

def solnaciente (request):
    return render(request, 'core/solnaciente.html')

def pintura2 (request):
    return render(request, 'core/pintura2.html')

def pintura3 (request):
    return render(request, 'core/pintura3.html')

def tipoarte(request):
    return render(request, 'core/paginatipoarte.html')

def apiobras(request):
    return render(request, 'core/apiobras.html')

def tablaobra(request):
    obras = Obra.objects.all()
    return render (request, 'core/hometabla.html', {'obras': obras })
    
def tabla (request):
    datos = {'form' : obraForm()}
    if request.method == 'POST':
        formulario = obraForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['form'] = formulario
            datos['color'] = "success"
            datos['mensaje'] = "Datos guardados" 
    else:
        datos['form'] = obraForm()
    return render (request, 'core/tablaobras.html', datos)

def modificar (request, autor):
    datos = {}
    obra = Obra.objects.get(autor = autor)
    if request.method == 'POST':
        formulario = obraForm(request.POST, instance=obra)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "obra modificada"
    datos['form']= obraForm(instance = obra)
    return render (request, 'core/modificar.html', datos)

def eliminar (request, autor):
    obra = Obra.objects.get(autor = autor)
    obra.delete()
    return redirect(to="home")