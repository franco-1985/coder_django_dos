from django.shortcuts import render
from django.views.generic import TemplateView

from coderdjango.students.models import Familiar, Curso

class StudentView(TemplateView):
    template_name = 'students/index.html'

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     return super().get_context_data(**kwargs)


    def get(self, request, status=None):

        cursos = Curso.objects.all()

        #print(request.GET.get('edad'))
        context = {
            #'edad': request.GET.get('edad'),
            # 'list_test': [curso,Familiar(),Familiar(),Familiar()]
            'list_test': cursos
        }
        return render(request, self.template_name, context)
