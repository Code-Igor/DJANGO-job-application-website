from django.shortcuts import render
from .forms import CandidaturaForm # import do forms

def home_view(request):
    return render(request, 'candidatura/home.html') #levando para a pagina home


def form_view(request):
    formulario = {
        "form":CandidaturaForm # passando o formulário pro html
    }
    return render(request, 'candidatura/form.html', formulario) # levando para a pagina do formulario

