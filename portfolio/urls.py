from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('ucs/', views.ucs_view, name='ucs'),
    path('docentes/', views.docentes_view, name='docentes'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
]