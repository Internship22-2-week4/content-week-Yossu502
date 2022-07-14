from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def helloWorld(request):
    return HttpResponse('Hello World')

urlpatterns = [
    path('helloWorld/', helloWorld)
]
