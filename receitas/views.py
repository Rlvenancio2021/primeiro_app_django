from django.shortcuts import render, get_list_or_404, get_object_or_404

# Importa o modelo do banco de dados para buscar as informações no banco.
from .models import Receita

# Create your views here.
def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
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

def buscar(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar'] # busca correspondente ao conteúdo da variável constante no enderço url apresentado na página busca "http://localhost:8000/busca?buscar=churrasco" nesse exemplo "churrasco"
        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)
            
    dados = {
        'receitas' : lista_receitas
    }
    
    return render(request, 'buscar.html', dados) # Cria caminha para página de busca. Um método para atender a requisição