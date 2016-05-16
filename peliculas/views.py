from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Peliculas

def listado(request):
	listado = Peliculas.objects()
	template = loader.get_template('tabla.html') 
	print (listado)
	context = {
		'listado': listado
	}

	return HttpResponse(template.render(context, request))

def registrar(request):
	if request.method == 'POST':
		pelicula = Peliculas(nombre=request.POST['nombre'], genero=request.POST['genero'], año=request.POST['ano'])
		pelicula.save()
		return HttpResponseRedirect('/')


	template = loader.get_template('index.html')
	context = {

	}

	return HttpResponse(template.render(context, request))	
