from django.shortcuts import render
from .models import (Licenciatura, UnidadeCurricular, Docente, Tecnologia,
                     Projeto, Competencia, Formacao, TFC, ExperienciaProfissional)
from escola.models import Curso, Aluno

def home_view(request):
    return render(request, 'portfolio/home.html', {
        'num_licenciaturas': Licenciatura.objects.count(),
        'num_ucs': UnidadeCurricular.objects.count(),
        'num_docentes': Docente.objects.count(),
        'num_projetos': Projeto.objects.count(),
        'num_tecnologias': Tecnologia.objects.count(),
        'num_competencias': Competencia.objects.count(),
        'num_formacoes': Formacao.objects.count(),
        'num_tfcs': TFC.objects.count(),
        'num_cursos': Curso.objects.count(),
        'num_alunos': Aluno.objects.count(),
    })

def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.prefetch_related('ucs').all()
    return render(request, 'portfolio/licenciaturas_list.html', {'licenciaturas': licenciaturas})

def ucs_view(request):
    ucs = UnidadeCurricular.objects.select_related('licenciatura').prefetch_related('docentes').all().order_by('ano', 'semestre')
    return render(request, 'portfolio/ucs_list.html', {'ucs': ucs})

def docentes_view(request):
    docentes = Docente.objects.prefetch_related('ucs').all()
    return render(request, 'portfolio/docentes_list.html', {'docentes': docentes})

def projetos_view(request):
    projetos = Projeto.objects.select_related('uc').prefetch_related('tecnologias').all()
    return render(request, 'portfolio/projetos_list.html', {'projetos': projetos})

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all().order_by('categoria', 'nome')
    return render(request, 'portfolio/tecnologias_list.html', {'tecnologias': tecnologias})

def competencias_view(request):
    competencias = Competencia.objects.prefetch_related('tecnologias', 'projetos', 'experiencias').all()
    return render(request, 'portfolio/competencias_list.html', {'competencias': competencias})

def formacoes_view(request):
    formacoes = Formacao.objects.all().order_by('data_inicio')
    return render(request, 'portfolio/formacoes_list.html', {'formacoes': formacoes})

def tfcs_view(request):
    tfcs = TFC.objects.prefetch_related('tecnologias').all().order_by('-interesse')
    return render(request, 'portfolio/tfcs_list.html', {'tfcs': tfcs})