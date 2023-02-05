from django.db import models
from django.utils import timezone

class user(models.Model):
    nome = models.CharField(max_length=20,blank=True)
    sobrenome = models.CharField(max_length=20, blank=True)
    usuario = models.CharField(max_length=20, blank=True)
    telefone = models.CharField(max_length=11 , blank = True)
    email = models.EmailField(max_length=50)
    data_criacao = models.DateTimeField(default=timezone.now)
    senha = models.CharField(max_length=16)
    
    
