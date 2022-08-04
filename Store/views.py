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

def categorias(request, id):
    #depto = ['Notebooks', 'Monitores', 'Impressoras']
    categ = Categoria.objects.filter(Departamento_id = id)
    depto = Departamento.objects.get(id = id)
    context = {'categorias': categ, 'departamento': depto}

    return render(request,'categorias.html', context)

    #produtos

def produtos(request, id):
    #depto = ['Notebooks', 'Monitores', 'Impressoras']
    pdt = Produto.objects.filter(categoria_id = id)
    categ = Categoria.objects.get(id = id)
    context = {'produtos': pdt, 'categorias': categ}
    
def produtos_detalhe(request, id):
    #depto = ['Notebooks', 'Monitores', 'Impressoras']
    categ = Produto.objects.get(id = id)
    depto = Departamento.objects.get(id = id)
    context = {'produtos_detalhe': categ}
    
    return render(request,'produtos_detalhe.html', context)