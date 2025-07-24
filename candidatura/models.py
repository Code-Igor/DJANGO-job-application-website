from django.db import models

# criando o model para o formulário, armazenando assim os dados obtidos
class CandidaturaModel(models.Model):
    nome_completo = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    email = models.EmailField()
    resposta = models.TextField()
    data_candidatura = models.DateTimeField(auto_now_add=True) # assim que for feito o envio do formulário, registrará a data