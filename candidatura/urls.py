# colocando as rotas aqui, 
# provavlemente terá só uma, porém caso eu queira criar mais páginas eu já vou deixar tudo
# certinho para possibilitar isso.

from django.urls import path
from . import views # importando as funções da views

app_name = "candidatura"

urlpatterns = [ 
    
    path('', views.home_view, name = "home"), #home da candidatura
    path("formulario/", views.form_view, name = "formulario") #rota do formulario
]