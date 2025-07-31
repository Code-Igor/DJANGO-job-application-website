from django.shortcuts import render, redirect 
from .forms import CandidaturaForm # import do form que criei
from django.http import HttpRequest


def home_view(request):
    return render(request, 'candidatura/candidaturaHome.html') #levando para a pagina home da candidatura


def form_view(request:HttpRequest): #tipando o meu request
    #abaixo estou salvando as informações conseguidas no formulario
    if request.method == "POST":
        formulario = CandidaturaForm(request.POST) 
        if formulario.is_valid():
            formulario.save() 
            return redirect("") #depois de ter validado o formulario e salvado, o usuario volta para a home

    formulario = {
        "form":CandidaturaForm # passando o formulário pro html
    }
    return render(request, 'candidatura/form.html', formulario) # levando para a pagina do formulario

