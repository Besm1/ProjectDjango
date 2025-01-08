from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def func_template(request):
    return render(request, 'func_page.html')

class ClassTemplate(TemplateView):
    template_name = 'class_page.html'
