from django.contrib import admin

# Importa o modelo de Receitas para o admin
from .models import Receita

# Classe criada para melhorar a visualização das receitas na página Admin
class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'publicada') # Nomes dos campos conforme o bando de dados
    list_display_links = ('id', 'nome_receita') # Transforma os conteúdos dos campos como links clicáveis.
    '''
    No caso dos campos de pesquisa para que funcionem é necessário que sejam lista ou tuplas,
    por esse motivo é necessário incluir uma "," virgula no final, caso contrário irá apresentar erro.
    '''
    search_fields = ('nome_receita',) # Adiciona campo de busca
    list_filter = ('categoria',) # Adiciona filtro por um campo específico
    list_per_page = 3 # Adiciona páginação, determina quantos resultadores serão exibidos por página
    list_editable = ('publicada',) # Torna o campo editável na seleção do Admin

# Register your models here.
admin.site.register(Receita, ListandoReceitas)