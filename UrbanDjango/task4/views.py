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
    extra_context = {'services':['Поездка за город с пьянкой и плясками под луной negligee      ... 15 000 руб./час ...'
        , "Заправка под завязку фирменным коктейлем и виски из самовара ...  5 000 руб./чел. ..."
        , 'ВНИМАНИЕ -- АКЦИЯ!!! Поездка в любом направлении без пьянки и песнопений ... Бесплатно!!! ...'
                                 ]}

class SpareParts(TemplateView):
    template_name = 'parts_price.html'
    extra_context = {'parts':["Руль спортивный из рогов антилопы гну ... извините, нет в продаже ..."
                     , "Шланг бензиновый                      ... извините, не завезли    ..."
                     , 'Коктейль фирменный "Эх, прокачу!" ... 500 руб. ...'
                     , 'Виски "Johnny Driver" ... 750 руб. ...'
                     ]}

