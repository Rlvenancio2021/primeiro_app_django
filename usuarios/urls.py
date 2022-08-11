# Primeiro foi criado o arquivo "urls.py" dentro da pasta "receitas".
# Para utilizar as urls do Django é necessário realizar a importação
from django.urls import path


# Necessário importar todas as urls e todas as veiws dela
# Views é para demonstrar qual arquivo exibir no navegador
from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadasro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
]
