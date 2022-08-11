from django.urls import path

from Store.models import Departamento
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('teste/', views.teste, name='teste'),
    path('Departamentos/', views.Departamentos,name='departamentos'),
    path('categorias/<int:id>', views.categorias,name='categorias'),
    path('produtos/<int:id>', views.produtos,name='produtos'),
    path('produtos_detalhe/<int:id>', views.produtos_detalhe, name='produto_detalhe'),
    path('institucional/', views.institucional, name='institucional'),
    path('contato/', views.contato, name='contato'),
    path('contato/enviar', views.enviar_email, name='enviar_email'),
]