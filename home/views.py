from django.shortcuts import render

def index(request):
    return render(request, 'home/homepage.html')

def login(request):
    return render(request, 'login/loginpage.html')

def cadastro(request):
    return render(request, 'login/cadastro.html')