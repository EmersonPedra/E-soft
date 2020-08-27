from django import forms 
from .models import Pessoa

class pessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('nome','sobrenome','idade','nascimento','email','apelido','observacao') #Campos do meu formulario 