import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.core.files import File
from portfolio.models import Docente, UnidadeCurricular, Tecnologia, Projeto, Formacao, MakingOf
from escola.models import Curso

def migrar(objetos, campo):
    for obj in objetos:
        field = getattr(obj, campo)
        if field and field.name:
            local_path = os.path.join('media', field.name)
            if os.path.exists(local_path):
                with open(local_path, 'rb') as f:
                    getattr(obj, campo).save(os.path.basename(local_path), File(f), save=True)
                print(f'Migrado: {obj} [{campo}]')

migrar(Docente.objects.all(), 'foto')
migrar(UnidadeCurricular.objects.all(), 'imagem')
migrar(Tecnologia.objects.all(), 'logo')
migrar(Projeto.objects.all(), 'imagem')
migrar(Formacao.objects.all(), 'certificado')
migrar(MakingOf.objects.all(), 'foto')
migrar(MakingOf.objects.all(), 'foto2')
migrar(MakingOf.objects.all(), 'foto3')
migrar(MakingOf.objects.all(), 'foto4')
migrar(MakingOf.objects.all(), 'foto5')
migrar(Curso.objects.all(), 'imagem')

print('Migração concluída!')