from django.shortcuts import render
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.models import User


def index(request):
    return render(request, 'home/homepage.html')

def login(request):
    return render(request, 'login/loginpage.html')

def cadastro(request):
    if request.method != 'POST':
        return render(request, 'login/cadastro.html')

    nome = request.POST.get('nome')
    usuario = request.POST.get('usuario')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    telefone = request.POST.get('telefone')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')
    
    if not nome:
        messages.error(request,"Nome não pode ser vazio")
        return render(request, 'login/cadastro.html')
    if not sobrenome:
        messages.error(request,"sobrenome não pode ser vazio")
        return render(request, 'login/cadastro.html')
    if not email:
        messages.error(request,"email não pode ser vazio")
        return render(request, 'login/cadastro.html')
    if not telefone:
        messages.error(request,"telefone não pode ser vazio")
        return render(request, 'login/cadastro.html')
    if not senha:
        messages.error(request,"senha não pode ser vazia")
        return render(request, 'login/cadastro.html')
    
    try:
        validate_email(email)
    except:
        messages.error(request,"email invalido. Ex.: email@example.com")
        return render(request, 'login/cadastro.html')
    
    if len(senha) <6:
         messages.error(request,"senha deve ter no minimo 6 caracteres")
         return render(request, 'login/cadastro.html')
     
    if User.objects.filter(email=email).exists():
         messages.error(request,"Email já cadastrado")
         return render(request, 'login/cadastro.html')