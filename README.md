# Primeiro projeto com Django.

## Bem vindo do meu projeto.

### Tecnologias que estou me dedicando atualmente
<div style="display: inline_block"><br/>
  <img aling="center" alt="Python3" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img aling="center" alt="Django3" src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">
  <img aling="center" alt="Postgres" src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white">
</div>

### Do Programa

Site de receitas culinárias para serem compartilhadas com amigos, basta realizar login e cadastrar a sua receita. Pode ser exibido para todos ou apenas para o usuário que cadastrou a receita.

### Como funciona

Como boa prática para proteção do projeto, sempre criar um ambiente virtual e ativa-lo, assim mantemos um ambiente individualizado para instalação de pacotes e ferramentas evitando problemas de versionamento.
Comando para MacOS ou Linux:
  Irá criar uma pasta com o nome "venv"
  ```
  python3 -m venv ./venv
  ```
  Ativar o ambiente virtual, irá aparecer o a palavra "(venv)" na linha do terminal
  ```
  source venv/bin/activate
  ```
  Para desativar o ambiente virtual ```deactivate```


Copiando esse projeto, será necessário instalar, POSTGRE (Banco de dados SQL), Framework DJANGO, pacote **Pillow** - para lidar com armazenamento de imagens no Python e **psycopg2** para conectação do Python com o Postgres.

Comando para instalação do Pillow
```pip install pillow```

Não esquercer de criar um super usuário para o Django, para acesso a página Admin, comando abaixo:
```
python manage.py createsuperuser
```
Na pasta Templates será possível observar todas as páginas que foram criadas para este projeto, inclusive as **partials** - uma forma muito interessante em Python para deixar o código ainda mais reutilizável e de fácil manutenção.

Os modelos de banco de dados podem ser verificados no arquivo *models.py* tanto da tabela PESSOA quanto RECEITA. Como o banco de dados irá guardar o endereço de cada imagem a ser anexada das receitas quando realizar o Upload, a imagem será gravada na pasta **media/fotos** na data que foi carregada.


###### Estou desenvolvendo este projeto acompanhando um curso e por este motivo os commit estão bem detalhados, apenas para servir como um guia futuramente.
