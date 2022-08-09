from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    # alteração para que quando utilizarmos a refereência, seja apresentado o campo que será refornado com essa função.
    def __str__(self):
        return self.nome