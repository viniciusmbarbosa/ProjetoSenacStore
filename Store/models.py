from distutils.command.upload import upload
from unicodedata import category
from django.db import models

# Create your models here.
class Departamento(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
         return self.nome

# Produtos!

class Produto(models.Model):
    nome = models.CharField(max_length=30)
    descrição = models.TextField(max_length=8000)
    imagem = models.ImageField(upload_to='images/')
    preco = models.DecimalField(max_digits=10,decimal_places=2)

    estoque = models.IntegerField()
    lancamento = models.BooleanField()
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)

    def __str__(self):
        return self.nome