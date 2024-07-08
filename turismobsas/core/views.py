from django.shortcuts import render, HttpResponse
#Create your views here.


def home(request):
       return render(request, "core/home.html")

def inicio(request):
    return render(request, "core/inicio.html")

def quienessomos(request):
    return render(request, "core/quienessomos.html")


def gandara(request):
    return render(request, "core/gandara.html")

def manzanares(request):
    return render(request, "core/manzanares.html")
    
def urube(request):
    return render(request, "core/urube.html")

def villaramallo(request):
    return render(request, "core/villaramallo.html")

def carlosken(request):
    return render(request, "core/carlosken.html")
def delcarril(request):
    return render(request, "core/delcarril.html")