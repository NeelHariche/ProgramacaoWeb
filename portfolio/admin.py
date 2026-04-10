from django.contrib import admin
from .models import (Licenciatura, Docente, UnidadeCurricular, Tecnologia,
                     Projeto, Competencia, Formacao, TFC,
                     ExperienciaProfissional, MakingOf)

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'instituicao', 'ano_inicio']
    search_fields = ['nome', 'instituicao']

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email']
    search_fields = ['nome', 'email']

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ano', 'semestre', 'ects', 'licenciatura']
    list_filter = ['ano', 'semestre', 'licenciatura']
    search_fields = ['nome']

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'nivel']
    list_filter = ['categoria', 'nivel']
    search_fields = ['nome']

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ano', 'uc']
    list_filter = ['ano', 'uc']
    search_fields = ['nome', 'descricao']

@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo']
    list_filter = ['tipo']
    search_fields = ['nome']

@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'instituicao', 'data_inicio', 'data_fim']
    list_filter = ['instituicao']
    search_fields = ['nome', 'instituicao']

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'ano']
    list_filter = ['ano']
    search_fields = ['titulo', 'autor']

@admin.register(ExperienciaProfissional)
class ExperienciaProfissionalAdmin(admin.ModelAdmin):
    list_display = ['cargo', 'empresa', 'data_inicio', 'data_fim']
    search_fields = ['cargo', 'empresa']

@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'entidade_relacionada', 'data']
    list_filter = ['entidade_relacionada']
    search_fields = ['titulo', 'descricao']