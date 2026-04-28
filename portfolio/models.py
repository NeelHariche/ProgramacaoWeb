from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=150)
    instituicao = models.CharField(max_length=150, default='Universidade Lusófona')
    ano_inicio = models.IntegerField()
    descricao = models.TextField(blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    foto = models.ImageField(upload_to='docentes/', blank=True, null=True)
    url_pagina_lusofona = models.URLField(blank=True)
    def __str__(self):
        return self.nome



class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=150)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='ucs')
    docentes = models.ManyToManyField(Docente, blank=True, related_name='ucs')

    def __str__(self):
        return self.nome



class Tecnologia(models.Model):
    NIVEL_CHOICES = [(1,'Básico'),(2,'Intermédio'),(3,'Avançado')]
    CATEGORIA_CHOICES = [('linguagem','Linguagem'),('framework','Framework'),
                         ('bd','Base de Dados'),('ferramenta','Ferramenta'),('outro','Outro')]
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    url_tecnologia = models.URLField(blank=True)
    destaque = models.TextField(blank=True, help_text='O que de mais relevante aprendeste')
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    nivel = models.IntegerField(choices=NIVEL_CHOICES, default=1)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    ano = models.IntegerField()
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    url_repositorio = models.URLField(blank=True)
    uc = models.ForeignKey(UnidadeCurricular, on_delete=models.SET_NULL,
                           null=True, blank=True, related_name='projetos')
    tecnologias = models.ManyToManyField(Tecnologia, blank=True, related_name='projetos')

    def __str__(self):
        return self.nome


class Competencia(models.Model):
    TIPO_CHOICES = [('tecnica','Técnica'),('soft','Soft Skill'),('outro','Outro')]
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descricao = models.TextField(blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True, related_name='competencias')
    projetos = models.ManyToManyField(Projeto, blank=True, related_name='competencias')
    experiencias = models.ManyToManyField('ExperienciaProfissional',blank=True,related_name='competencias_adquiridas')

    def __str__(self):
        return self.nome



class Formacao(models.Model):
    nome = models.CharField(max_length=150)
    instituicao = models.CharField(max_length=150)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    descricao = models.TextField(blank=True)
    certificado = models.FileField(upload_to='formacoes/', blank=True, null=True)
    url = models.URLField(blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True, related_name='formacoes')
    competencias = models.ManyToManyField(Competencia, blank=True, related_name='formacoes')

    def __str__(self):
        return self.nome



class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    orientador = models.CharField(max_length=150, blank=True)
    ano = models.IntegerField()
    descricao = models.TextField(blank=True)
    url_repositorio = models.URLField(blank=True)
    interesse = models.IntegerField(default=1, help_text='1 a 5 — nível de interesse')
    tecnologias = models.ManyToManyField(Tecnologia, blank=True, related_name='tfcs')
    competencias = models.ManyToManyField(Competencia, blank=True, related_name='tfcs')

    def __str__(self):
        return self.titulo



class ExperienciaProfissional(models.Model):
    empresa = models.CharField(max_length=150)
    cargo = models.CharField(max_length=150)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    descricao_Empresa = models.TextField(blank=True)
    descricao_Cargo = models.TextField(blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True, related_name='experiencias')
    

    def __str__(self):
        return f'{self.cargo} @ {self.empresa}'



class MakingOf(models.Model):
    ENTIDADE_CHOICES = [
        ('licenciatura','Licenciatura'),
        ('uc','Unidade Curricular'),
        ('projeto','Projeto'),
        ('tecnologia','Tecnologia'),
        ('competencia','Competência'),
        ('formacao','Formação'),
        ('tfc','TFC'),
        ('experiencia','Experiência Profissional'),
        ('MakingOf','MakingOf'),
    ]
    titulo = models.CharField(max_length=200)
    entidade_relacionada = models.CharField(max_length=30, choices=ENTIDADE_CHOICES)
    descricao = models.TextField()
    decisoes_tomadas = models.TextField(blank=True)
    justificacao_modelacao = models.TextField(blank=True)  
    erros_encontrados = models.TextField(blank=True)
    correcoes = models.TextField(blank=True)
    uso_ia = models.TextField(blank=True)
    foto = models.ImageField(upload_to='makingof/', blank=True, null=True)
    foto2 = models.ImageField(upload_to='makingof/', blank=True, null=True)  
    foto3 = models.ImageField(upload_to='makingof/', blank=True, null=True)  
    foto4 = models.ImageField(upload_to='makingof/', blank=True, null=True) 
    foto5 = models.ImageField(upload_to='makingof/', blank=True, null=True) 

    def __str__(self):
        return self.titulo

