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
    extra_context = {'s1':'Поездка за город с пьянкой и плясками под луной negligee      ... 15 000 руб./час ...'
                     , 's2':"Заправка под завязку фирменным коктейлем и виски из самовара ...  5 000 руб./чел. ..."
                     , 's3':"Поездка в любом направлении без пьянки и песнопений          ... Бесплатно!!! ..."}

class SpareParts(TemplateView):
    template_name = 'parts_price.html'
    extra_context = {'s1':"Руль спортивный из рогов антилопы гну ... извините, нет в продаже ..."
                     , 's2':"Шланг бензиновый                      ... извините, не завезли    ..."
                     , 's3':'Коктейль фирменный "Эх, прокачу!" ... 500 руб. ...'
                     , 's4':'Виски "Johnny Driver" ... 750 руб. ...'
                     }

