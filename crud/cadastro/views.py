from django.shortcuts import render,redirect,get_object_or_404
from .models import Pessoa
from .forms import pessoaForm
from django.contrib import messages
from django.core.paginator import Paginator
from .services import get_random_name

def listPessoa(request):
    
    # Parte responsavel pela barra de busca    
    search = request.GET.get('search')
    
    if search:
        pessoas = Pessoa.objects.filter(nome__icontains = search).order_by('nome','sobrenome')
    else:    
        lista_pessoas = Pessoa.objects.all().order_by('nome','sobrenome')
        # Essa parte do código é responsavel pelo sistema de paginação
        paginador = Paginator(lista_pessoas,5)
        page = request.GET.get('page')
        pessoas = paginador.get_page(page)

    return render(request, 'cadastroPessoas/listPessoa.html', {'pessoas': pessoas})

def createPessoa(request):

    # Essa parte pega os dados fornecidos pela api e divide em nome e sobrenome
    nome = get_random_name()
    primeiro_nome = nome[0]
    sobrenome = ""
    sobrenome = '_'.join(nome[1::])
    
           
    if  request.method == "POST":
        form = pessoaForm(request.POST)
        if form.is_valid(): # Verifica se o formulario é válido antes de salvar os dados
            pessoa = form.save(commit=False)
            pessoa.save()
            
            #Envia uma mensagem confirmando que a pessoa foi cadastrada no sistema
            messages.info(request, 'A pessoa foi cadastrada com sucesso.')
            return redirect('/listPessoa')


    else:
        form = pessoaForm()
        return render(request,'cadastroPessoas/createPessoa.html', {'form': form,'nome':primeiro_nome,
        'sobrenome': sobrenome})

def updatePessoa(request,id):
    pessoa = get_object_or_404(Pessoa,pk=id)
    form = pessoaForm(instance=pessoa)
    if request.method == "POST":
        form = pessoaForm(request.POST, instance=pessoa)
        if (form.is_valid()): #Verifica se o formulario é válido e salva 
            pessoa.save()

            #Envia uma mensagem confirmando que o dado foi alterado
            messages.info(request, 'O registro foi alterado com sucesso.')
            return redirect('/listPessoa')
        else: #Caso nao seja válido retorna para a página de edição
            return render(request,"cadastroPessoas/updatePessoa.html",{'form': form,'pessoa':pessoa})

    else:
        return render(request,"cadastroPessoas/updatePessoa.html",{'form': form,'pessoa':pessoa})

def deletePessoa(request,id):
    pessoa = get_object_or_404(Pessoa,pk=id)
    pessoa.delete()

    #Envia uma mensagem confirmando que o dado foi deletado do registro
    messages.info(request, 'O registro foi deletado com sucesso.')
    return redirect('/listPessoa')
