# Primeiro foi criado o arquivo "urls.py" dentro da pasta "receitas".
# Para utilizar as urls do Django é necessário realizar a importação
from django.urls import path


# Necessário importar todas as urls e todas as veiws dela
# Views é para demonstrar qual arquivo exibir no navegador
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
