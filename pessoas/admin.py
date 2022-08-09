from django.contrib import admin
from .models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email') # Nomes dos campos conforme o bando de dados
    list_display_links = ('id', 'nome',) # Transforma os conteúdos dos campos como links clicáveis.
    '''
    No caso dos campos de pesquisa para que funcionem é necessário que sejam lista ou tuplas,
    por esse motivo é necessário incluir uma "," virgula no final, caso contrário irá apresentar erro.
    '''
    search_fields = ('nome',) # Adiciona campo de busca
    list_per_page = 3 # Adiciona páginação, determina quantos resultadores serão exibidos por página

# Register your models here.
admin.site.register(Pessoa, ListandoPessoas)