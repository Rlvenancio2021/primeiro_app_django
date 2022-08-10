from django.db import models
from datetime import datetime
from pessoas.models import Pessoa

# Create your models here.
class Receita(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE) # Cria uma vinculação dos dados entre os banco de dados
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True) # blank para caso não for possível pegar a informação, pode deixar em branco.
    publicada = models.BooleanField(default=False) # Cria um campo para flag de publicação
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
    def __str__(self):
        return self.nome_receita