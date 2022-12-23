from django.shortcuts import render,redirect
from .models import *
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

def gestionIndicador(request):
    indicadorList=indicador.objects.all()
    return render(request, 'gestionIndicador.html', {"indicadorList":indicadorList})#se le pasa por parametro {"criteriosMedidasList":criteriosMedidasList}    

def registrarIndicador(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    descripcion=request.POST['txtdescripcion']
    peso=request.POST['txtpeso']
    
    IndicadorL=indicador.objects.create(
        codigo=codigo,nombre=nombre,descripcion=descripcion,peso=peso)
    return redirect('/gestionIndicador/')
def eliminarIndicador(request,codigo):
    Indicador=indicador.objects.get(codigo=codigo)
    Indicador.delete()
    return redirect('/gestionIndicador/')
def editarIndicador(request,codigo):
    Indicador=indicador.objects.get(codigo=codigo)
    return render(request,"editarIndicador.html",{"indicador":Indicador})
def editarIndicador2(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    descripcion=request.POST['txtdescripcion']
    peso=request.POST['txtpeso']
    
    Indicador=indicador.objects.get(codigo=codigo)
    Indicador.nombre=nombre
    Indicador.descripcion=descripcion
    Indicador.peso=peso
    Indicador.save()
    return redirect('/gestionIndicador/')