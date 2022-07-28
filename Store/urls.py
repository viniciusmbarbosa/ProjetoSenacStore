from django.urls import path

from Store.models import Departamento
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('teste/', views.teste, name='teste'),
    path('Departamentos/', views.Departamentos,name='departamentos'),
    path('categorias/', views.categorias,name='categorias'),
    path('produtos/', views.produtos,name='produtos')
]