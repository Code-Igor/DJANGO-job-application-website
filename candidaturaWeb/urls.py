from django.contrib import admin
from django.urls import path, include
from . import views # importando as funções da views

# urls principais do site
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view), # cai direto aqui ao abrir
    path('candidatura/', include("candidatura.urls")) # vai para as paginas de canddiatura
]
