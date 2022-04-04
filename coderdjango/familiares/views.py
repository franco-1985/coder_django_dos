from django.shortcuts import render
from django.views.generic import TemplateView

from coderdjango.familiares.models import Familiar

class FamiliaView(TemplateView):
    template_name = 'familiares/index.html'

    def get(self, request, status=None):
        familiares = Familiar.objects.all()

        context = {
            'list_test': familiares
        }
        return render(request, self.template_name, context)
