from django.http import HttpRequest
from django.shortcuts import render
from inicioApp.forms import formularioafi
from inicioApp.models import aficionado
from django.contrib.auth.decorators import login_required



#Create your views here.

@login_required
def index(request):
    return render(request,  'registration/login.html')


def inicioDef(request):
      return render(request,'inicio.html',{})

def port1(request):
      return render(request,'portafolio.html',{})



#def  registro(request):
   #   return render(request, 'registro.html')


class formularioafiview(HttpRequest):
      def index(request):
            aficionado=formularioafi()
            return render(request, "afiindex.html", {"form":aficionado})
      def procesar_formulario(request):
            aficionado=formularioafi(request.POST)
            if aficionado.is_valid():
                  aficionado.save()
                  aficionado=formularioafi()
            return render(request, "afiindex.html", {"form":aficionado, "mensaje": 'ok'})

      def listar_aficionados(request):
            aficionados = aficionado.objects.all()
            return render(request,"listaaficionados.html ",{"aficionados" : aficionados})

      def edit(request, id_aficionado):
            aficionados= aficionado.objects.filter(id=id_aficionado).first()
            form = formularioafi(instance=aficionados)
            return render(request,"aficionadoedit.html",{"form":form, 'aficionado': aficionados})

      def actualizar_aficionado(request, id_aficionado,):
            aficionados=aficionado.objects.get(pk=id_aficionado)
            form= formularioafi(request.POST, instance=aficionados)
            if form.is_valid():
                  form.save()
            aficionados=aficionado.objects.all()
            return render(request,"listaaficionados.html",{"aficionados":aficionados})


      def delete(request,id_aficionado):
            aficionados = aficionado.objects.get(pk=id_aficionado)
            aficionados.delete()
            aficionados = aficionado.objects.all()
            return render(request,"listaaficionados.html",{"aficionados": aficionados, "mensaje": 'Ok'})



