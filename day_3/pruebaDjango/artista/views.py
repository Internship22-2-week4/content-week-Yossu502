from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
  print(request)
  return HttpResponse('Pagina para agregar artistas')