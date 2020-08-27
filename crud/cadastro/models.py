from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    sobrenome = models.CharField(max_length=100,blank=False)
    idade = models.IntegerField(blank=False)
    nascimento = models.DateField(blank=False)
    email = models.EmailField(blank=False)
    apelido = models.CharField(max_length=100,blank=True)
    observacao = models.TextField(blank=True)

# Registros para ter um controle da data de criação e alteração dos dados 
# Não foi pedido, porem é uma boa prática

    data_de_criacao = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome