from django import forms
from .models import CandidaturaModel

class CandidaturaForm(forms.ModelForm):
    class Meta:
        model = CandidaturaModel
        fields = ['nome_completo', 'idade', 'email', 'resposta']
