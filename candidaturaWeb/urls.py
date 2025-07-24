from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # tirar isso aqui path('', views.index_view) # path da home
    path('candidatura/', include("candidatura.urls")) #adicionando o path do formulario
]
