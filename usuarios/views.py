from django.shortcuts import render, redirect, get_object_or_404 # Para pegar a "pessoa" da requisição
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita
'''
Realizar importação do modelo de Receitas, para possibilitar a criação de um objeto de Receita dentro veiws de usuário.
'''

# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome'] # Busca o dado da requisição conforme o método POST
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            messages.warning(request, 'O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            messages.warning(request, 'O campo e-mail não pode ficar em branco')
            return redirect('cadastro')
        if senha != senha2:
            messages.error(request, 'As senhas não são iguais !!')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists(): # Função que verificar se o usuário já existe. Para este uso é necessário importar a bibliteca User.
            messages.warning(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha) # Cria um objeto para o usuário que deseja cadastrar.
        user.save() # função que grava o usuário no banco de dados.
        messages.success(request, 'Cadastro realizado com sucesso !!')
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
        id = request.user.id
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa = id)
        dados = {
            'receitas': receitas
        }
        return render(request, 'usuarios/dashboard.html', dados)
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
        user = get_object_or_404(User, pk=request.user.id) # Para pegar a "pessoa" da requisição
        receita = Receita.objects.create(
            pessoa = user,
            nome_receita = nome_receita,
            ingredientes = ingredientes,
            modo_preparo = modo_preparo,
            tempo_preparo = tempo_preparo,
            rendimento = rendimento,
            categoria = categoria,
            foto_receita = foto_receita
        ) # Cria o objeto receita com base na classe Receita (Banco de Dados)
        receita.save() # Registra receita criado no banco de dados.
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_receita.html')