from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.artigos_list, name='list'),
    path('<int:pk>/', views.artigo_detail, name='detail'),
    path('criar/', views.artigo_create, name='create'),
    path('<int:pk>/editar/', views.artigo_edit, name='edit'),
    path('<int:pk>/apagar/', views.artigo_delete, name='delete'),
    path('<int:pk>/like/', views.artigo_like, name='like'),
    path('<int:pk>/comentar/', views.comentario_create, name='comentar'),
]