from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
#
# def func_template(request):
#     return render(request, 'func_page.html')

class AutoShop(TemplateView):
    template_name = 'AutoShop_main.html'

class Service(TemplateView):
    template_name = 'service_price.html'

class SpareParts(TemplateView):
    template_name = 'parts_price.html'

