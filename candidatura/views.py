import openpyxl
from .models import CandidaturaModel
from django.shortcuts import render, redirect 
from .forms import CandidaturaForm # import do form que criei
from django.http import HttpRequest
from django.http import HttpResponse

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



#view para gerar um relatório excel com as respostas do formulário

def exportar_candidaturas_view(request):
    # cria um novo workbook (arquivo Excel)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Candidaturas Analista de Sistema Júnior"

    # cabeçalho
    ws.append(["Nome Completo", "Idade", "Email", "Resposta"])

    # dados do banco
    for candidatura in CandidaturaModel.objects.all():
        ws.append([candidatura.nome_completo, candidatura.idade, candidatura.email, candidatura.resposta ])

    # criar resposta HTTP para download
    # basicamente ao acessar a página pela url certa (candidatura/candidaturas_excel/) o dowload do arquivo xlsx é baixado automaticamente
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=candidaturas.xlsx'
    wb.save(response)
    return response