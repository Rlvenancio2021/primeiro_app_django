from django.shortcuts import render, redirect
from django.contrib.auth.models import User

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
    return render(request, 'usuarios/login.html')

def logout(request):
    pass

def dashboard(request):
    pass