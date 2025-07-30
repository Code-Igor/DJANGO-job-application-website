from django import forms
from .models import CandidaturaModel

class CandidaturaForm(forms.ModelForm):
    class Meta:
        model = CandidaturaModel
        fields = ['nome_completo', 'idade', 'email', 'resposta']

        #utilizando widgets para personalizar o formulario
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'reposta': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
