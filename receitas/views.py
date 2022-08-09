from django.shortcuts import render, get_list_or_404, get_object_or_404

# Importa o modelo do banco de dados para buscar as informações no banco.
from .models import Receita

# Create your views here.
def index(request):
    receitas = Receita.objects.filter(publicada=True)
    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', dados)

# Estrutura alterada para capturar o ID da receita será exibida no endereço da URL no site.
def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_exibir = {
        'receita': receita
    }
    return render(request, 'receita.html', receita_a_exibir)