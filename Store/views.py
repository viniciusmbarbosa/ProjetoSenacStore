from django.shortcuts import render
from django.http import HttpResponse

from Store.models import Categoria, Departamento, Produto
# Create your views here.
def index(request):
    meu_nome = 'Lojas brasil'
    sexo = 'M'
    context = {
        'nome': meu_nome,
        'artigo': 'o' if sexo == 'M' else 'a'
        }
    return render(request,'index.html', context)

def teste(request):
    #depto = ['Casa', 'informatica', 'Telefonia']
    depto = Departamento.objects.all()
    context = {'departamentos': depto}
    
    return render(request,'teste.html', context)

    #Departamento.html

def Departamentos(request):
    #depto = ['Casa', 'informatica', 'Telefonia']
    depto = Departamento.objects.all()
    context = {'departamentos': depto}

    return render(request,'Departamentos.html', context)

    #Categotias

def categorias(request):
    #depto = ['Notebooks', 'Monitores', 'Impressoras']
    categ = Categoria.objects.all()
    context = {'categorias': categ}

    return render(request,'categorias.html', context)

    #produtos

def produtos(request):
    #depto = ['Notebooks', 'Monitores', 'Impressoras']
    pdt = Produto.objects.all()
    context = {'produtos': pdt}

    return render(request,'produtos.html', context)