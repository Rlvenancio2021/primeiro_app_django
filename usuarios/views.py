from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome'] # Busca o dado da requisição conforme o método POST
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            print('O campo e-mail não pode ficar em branco')
            return redirect('cadastro')
        if senha != senha2:
            print('As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists(): # Função que verificar se o usuário já existe. Para este uso é necessário importar a bibliteca User.
            print('Usuário já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha) # Cria um objeto para o usuário que deseja cadastrar.
        user.save() # função que grava o usuário no banco de dados.
        print('Usuário cadastrado com sucesso!!')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            print('Os campos e-mail e senha não podem ficar em branco')
            return redirect('login')
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get() # Por esse objeto, filtar o e-mail que existe no banco de dados e retorna o nome do usuário.
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated: # Comando para validar se o usuário está de fato logado, caso não estiver será redirecionado para a home.
        return render(request, 'usuarios/dashboard.html')
    else:
        return redirect('index')
    
def cria_receita(request):
    if request.method == 'POST':
        # Dados conforme o cria_receita.html no elemento "name" de cada campo
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita'] # Para carregar arquivos
        print(nome_receita, ingredientes, modo_preparo, tempo_preparo, rendimento, categoria, foto_receita)
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_receita.html')