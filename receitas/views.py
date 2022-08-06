from django.shortcuts import render

# Importa o modelo do banco de dados para buscar as informações no banco.
from .models import Receita

# Create your views here.
def index(request):
    receitas = (Receita.objects.all) # Para o mdelo de receitas retornar todas as receitas existentes
    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')