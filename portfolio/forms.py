from django import forms
from .models import Projeto, Tecnologia, Competencia, Formacao

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'ano', 'imagem', 'url_repositorio', 'uc', 'tecnologias']

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = ['nome', 'categoria', 'nivel', 'logo', 'url_tecnologia', 'destaque']

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['nome', 'tipo', 'descricao', 'tecnologias', 'projetos', 'experiencias']

class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = ['nome', 'instituicao', 'data_inicio', 'data_fim', 'descricao', 'certificado', 'url', 'tecnologias', 'competencias']