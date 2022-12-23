from django.shortcuts import render,redirect
from .models import criteriomedida
# Create your views here.

def home(request):
    criteriosMedidasList=criteriomedida.objects.all()
    return render(request, 'gestionCriterioMedida.html', {"criteriosMedidasList":criteriosMedidasList})#se le pasa por parametro {"criteriosMedidasList":criteriosMedidasList}
    
def registrarCriterio(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    descripcion=request.POST['txtdescripcion']
    peso=request.POST['txtpeso']
    
    criterioMedidaL=criteriomedida.objects.create(
        codigo=codigo,nombre=nombre,descripcion=descripcion,peso=peso)
    return redirect('/')
def eliminarCriterio(request,codigo):
    criteriomedidas=criteriomedida.objects.get(codigo=codigo)
    criteriomedidas.delete()
    return redirect('/')
def editarCriterio(request,codigo):
    criteriomedidas=criteriomedida.objects.get(codigo=codigo)
    return render(request,"editarCriterio.html",{"criterio":criteriomedidas})
def editarCriterio2(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    descripcion=request.POST['txtdescripcion']
    peso=request.POST['txtpeso']
    
    criteriomedidas=criteriomedida.objects.get(codigo=codigo)
    criteriomedidas.nombre=nombre
    criteriomedidas.descripcion=descripcion
    criteriomedidas.peso=peso
    criteriomedidas.save()
    return redirect('/')