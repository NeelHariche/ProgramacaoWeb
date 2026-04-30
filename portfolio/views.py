from django.shortcuts import render, get_object_or_404, redirect
from .models import (Licenciatura, UnidadeCurricular, Docente, Tecnologia,
                     TipoTecnologia, Projeto, Competencia, Formacao, TFC,
                     ExperienciaProfissional, MakingOf)
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm
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
        'num_experiencias': ExperienciaProfissional.objects.count(),
    })

def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.prefetch_related('ucs').all()
    return render(request, 'portfolio/licenciaturas_list.html', {'licenciaturas': licenciaturas})

def docentes_view(request):
    docentes = Docente.objects.prefetch_related('ucs').all()
    return render(request, 'portfolio/docentes_list.html', {'docentes': docentes})

def ucs_view(request):
    ucs = UnidadeCurricular.objects.select_related('licenciatura').prefetch_related('docentes').all().order_by('ano', 'semestre')
    return render(request, 'portfolio/ucs_list.html', {'ucs': ucs})

def projetos_view(request):
    projetos = Projeto.objects.select_related('uc').prefetch_related('tecnologias').all()
    return render(request, 'portfolio/projetos_list.html', {'projetos': projetos})

def projeto_criar(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Novo Projeto', 'voltar': '/projetos/'})

def projeto_editar(request, pk):
    obj = get_object_or_404(Projeto, pk=pk)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': f'Editar {obj.nome}', 'voltar': '/projetos/'})

def projeto_apagar(request, pk):
    obj = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('projetos')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': obj, 'titulo': 'Apagar Projeto', 'voltar': '/projetos/'})

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all().order_by('categoria', 'nome')
    return render(request, 'portfolio/tecnologias_list.html', {'tecnologias': tecnologias})

def tecnologia_criar(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Nova Tecnologia', 'voltar': '/tecnologias/'})

def tecnologia_editar(request, pk):
    obj = get_object_or_404(Tecnologia, pk=pk)
    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': f'Editar {obj.nome}', 'voltar': '/tecnologias/'})

def tecnologia_apagar(request, pk):
    obj = get_object_or_404(Tecnologia, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('tecnologias')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': obj, 'titulo': 'Apagar Tecnologia', 'voltar': '/tecnologias/'})

def competencias_view(request):
    competencias = Competencia.objects.prefetch_related('tecnologias', 'projetos', 'experiencias').all()
    return render(request, 'portfolio/competencias_list.html', {'competencias': competencias})

def competencia_criar(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Nova Competência', 'voltar': '/competencias/'})

def competencia_editar(request, pk):
    obj = get_object_or_404(Competencia, pk=pk)
    form = CompetenciaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': f'Editar {obj.nome}', 'voltar': '/competencias/'})

def competencia_apagar(request, pk):
    obj = get_object_or_404(Competencia, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('competencias')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': obj, 'titulo': 'Apagar Competência', 'voltar': '/competencias/'})

def formacoes_view(request):
    formacoes = Formacao.objects.all().order_by('data_inicio')
    return render(request, 'portfolio/formacoes_list.html', {'formacoes': formacoes})

def formacao_criar(request):
    form = FormacaoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Nova Formação', 'voltar': '/formacoes/'})

def formacao_editar(request, pk):
    obj = get_object_or_404(Formacao, pk=pk)
    form = FormacaoForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': f'Editar {obj.nome}', 'voltar': '/formacoes/'})

def formacao_apagar(request, pk):
    obj = get_object_or_404(Formacao, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('formacoes')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': obj, 'titulo': 'Apagar Formação', 'voltar': '/formacoes/'})

def tfcs_view(request):
    tfcs = TFC.objects.prefetch_related('tecnologias').all().order_by('-interesse')
    return render(request, 'portfolio/tfcs_list.html', {'tfcs': tfcs})

def experiencias_view(request):
    experiencias = ExperienciaProfissional.objects.prefetch_related('tecnologias').all()
    return render(request, 'portfolio/experiencias_list.html', {'experiencias': experiencias})

def sobre_view(request):
    from .models import TipoTecnologia
    projeto_portfolio = Projeto.objects.filter(nome__icontains='Portfolio').first()
    tecnologias = projeto_portfolio.tecnologias.all() if projeto_portfolio else Tecnologia.objects.none()
    tipos = TipoTecnologia.objects.prefetch_related('tecnologias').all()
    makingofs = MakingOf.objects.all().order_by('id')[:3]
    mvt = MakingOf.objects.filter(titulo__icontains='MVT').first()
    der = MakingOf.objects.filter(titulo__icontains='DER').first()
    navegacao = MakingOf.objects.filter(titulo__icontains='navega').first()
    return render(request, 'portfolio/sobre.html', {
        'tecnologias': tecnologias,
        'tipos': tipos,
        'makingofs': makingofs,
        'github_url': 'https://github.com/NeelHariche/ProgramacaoWeb',
        'mvt': mvt,
        'der': der,
        'navegacao': navegacao,
    })

def makingof_view(request, pk=None):
    makingofs = MakingOf.objects.all().order_by('id')
    entrada = get_object_or_404(MakingOf, pk=pk) if pk else makingofs.first()
    return render(request, 'portfolio/makingof.html', {'entrada': entrada, 'makingofs': makingofs})