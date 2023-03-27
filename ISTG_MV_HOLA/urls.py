"""ISTG_MV_HOLA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    #1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from inicioApp import views
from inicioApp.views import formularioafiview


urlpatterns =[
    path('', views.inicioDef,name='inicio'),
    path('portafolio/', views.port1,name='port'),
    path('admin/', admin.site.urls),
    path('registraraficionado/', formularioafiview.index, name='registraraficionado'),
    path('guardaraficionado/', formularioafiview.procesar_formulario, name='guardaraficionado'),
    path('listaraficionados/', formularioafiview.listar_aficionados, name='listaraficionados'),
    path('editaraficionados/<id_aficionado>/',formularioafiview.edit, name='editaraficionados'),
    path('actualizaraficionados/<id_aficionado>/',formularioafiview.actualizar_aficionado, name='actualizaraficionados'),
    path('eliminaraficionados/<id_aficionado>/',formularioafiview.delete, name='eliminaraficionados'),
    path('accounts/',include('django.contrib.auth.urls')),

]