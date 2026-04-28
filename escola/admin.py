from django.contrib import admin
from .models import Curso, Professor, Aluno

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email']
    search_fields = ['nome']

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'numero']
    search_fields = ['nome', 'numero']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'professor']
    search_fields = ['nome']
    filter_horizontal = ['alunos']