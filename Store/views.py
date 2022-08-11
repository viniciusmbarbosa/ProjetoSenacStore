from django.shortcuts import render
from django.http import HttpResponse
from Store.models import Departamento
from Store.models import Categoria
from Store.models import Produto
from django.core.mail import send_mail

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

    
def contato(request):
    return render(request, 'contato.html')

def institucional(request):
    return render(request, 'institucional.html')

def enviar_email(request):
    name = request.POST['name']
    phone = request.POST['phone']
    assunto = request.POST['assunto']
    mensagem = request.POST['mensagem']
    remetente = request.POST['email']
    destinatario = ['viniciusdemirandabarbosa@gmail.com']
    corpo = f"name: {name} <br> \
            telefone:{phone} <br> \
            Mensagem: {mensagem}"
    
    try:
        send_mail(assunto, corpo, remetente, destinatario)
        context = {'msg': 'E-mail enviado com sucesso!'}
    except:
        context = {'msg': 'Erro ao enviar o Email!'}
    return render(request,'produtos_detalhe.html', context)