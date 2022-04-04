from django.shortcuts import render
from django.http import HttpRequest
#from django.views.generic import TemplateView

from coderdjango.familiares.models import Familiar
from coderdjango.familiares.forms import FormularioFamiliar

#class FamiliaView(TemplateView):
class FamiliaView(HttpRequest):

    def get(request, status=None):
        template_name = 'familiares/index.html'
        familiares = Familiar.objects.all()

        context = {
            'list_test': familiares
        }
        return render(request, template_name, context)

    def index(request):
        template_name = 'familiares/add.html'
        familiar = FormularioFamiliar()
        return render(request, template_name, {'form': familiar})

    def procesar_formulario(request):
        template_name = 'familiares/add.html'
        familiar= FormularioFamiliar(request.POST)
        if familiar.is_valid():
            familiar.save()
            familiar = FormularioFamiliar()
        return render(request, template_name, {'form': familiar, 'mensaje':'OK'})
