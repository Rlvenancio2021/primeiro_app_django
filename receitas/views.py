from django.shortcuts import render
# Para que possamos usar o request
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Receitas</h1> <h2>Bem vindo</h2>')