import json
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic import TemplateView

from .models import Legislature
from .models import ParliamentaryGroup

class LegislaturesView(TemplateView):
    template_name = "legislatures/legislatures.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        years = Legislature.objects.order_by('year').values('year').distinct()
        years_list = [year['year'] for year in years]
        types = Legislature.POLITICAL_SYSTEM_CHOICES

        series = []
        values = []

        for type, typename in types:
            legislatures = Legislature.objects.all().filter(system=type)
            data = []
            for year in years_list:
                year_as_date = '{}-01-01'.format(year)
                if legislatures.filter(year=year):
                    value = legislatures.filter(year=year).first().percentage
                    values.append(value)
                    data.append({
                        'year': year_as_date,
                        'value': value
                    })
            series.append({
                'name': typename,
                'data': data
            })

        parl_groups = ParliamentaryGroup.GROUP_CHOICES

        parl_series = []
        parl_values = []

        for choice, choicename in parl_groups:
            parl_group = ParliamentaryGroup.objects.all().filter(group=choice)
            data = []
            for year in years_list:
                year_as_date = '{}-01-01'.format(year)
                if parl_group.filter(legislature__year=year):
                    parl_group_first = parl_group.filter(legislature__year=year).first()
                    value = parl_group_first.percentage_women
                    parl_values.append(value)
                    if value is None:
                        info = 'Nicht im Parlament vertreten'
                    else:
                        info = ('Frauen: '
                                + str(parl_group_first.number_women)
                                + ' von '
                                + str(parl_group_first.number_group))
                    data.append({
                        'year': year_as_date,
                        'value': value,
                        'info': info
                    })
            parl_series.append({
                'name': choicename,
                'data': data
            })

        context['series'] = json.dumps(series, cls=DjangoJSONEncoder)
        context['years'] = json.dumps(years_list, cls=DjangoJSONEncoder)
        context['values'] = json.dumps(values, cls=DjangoJSONEncoder)
        context['parl_series'] = json.dumps(parl_series, cls=DjangoJSONEncoder)
        context['parl_values'] = json.dumps(parl_values, cls=DjangoJSONEncoder)
        return context

