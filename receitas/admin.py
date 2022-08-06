from django.contrib import admin

# Importa o modelo de Receitas para o admin
from .models import Receita


# Register your models here.
admin.site.register(Receita)