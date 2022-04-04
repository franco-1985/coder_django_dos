from django.shortcuts import render
from django.views.generic import TemplateView

from coderdjango.students.models import Familiar, Curso

class StudentView(TemplateView):
    template_name = 'students/index.html'

    def get(self, request, status=None):
        familiares = Familiar.objects.all()

        #print(request.GET.get('edad'))
        context = {
            #'edad': request.GET.get('edad'),
            'list_test': familiares
        }
        return render(request, self.template_name, context)

    def post(self, request):
        pass
