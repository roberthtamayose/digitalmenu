from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render (request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Usuário logado.')
        return redirect('dashboard')



def logout(request):
    auth.logout(request)
    return redirect('dashboard')


def register(request):
    if request.method != 'POST':
        ##messages.success(request, 'Cadastrado com sucesso')
        return render(request, 'accounts/register.html')

    nome = request.POST.get('nome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    if not nome or not email or not usuario or not senha:
        messages.error(request, 'Preencher todos os campos.')
        return render(request, 'accounts/register.html')

    try:
        validate_email(email)
    except: 
        messages.error(request, 'Email inválido.')
        return render(request, 'accounts/register.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'usuário já existe.')
        return render(request, 'accounts/register.html')

    messages.success(request, 'Registrado com sucesso!')

    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome)
    user.save()
    return redirect('index_login')


@login_required(redirect_field_name='')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
