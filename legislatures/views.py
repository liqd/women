import json
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic import TemplateView

from .models import ParliamentaryGroup
from .models import Legislature

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

        legislature = Legislature.objects.get(name='19. Bundestag')
        groups = ParliamentaryGroup.objects.filter(legislature=legislature)
        children = []
        for group in groups:
            children.append({
                'name': group.group,
                'colour': group.colour_code,
                'children': [
                    {'name': 'Frauen',
                     'size': group.number_women},
                    {'name': 'Männer',
                     'size': group.number_group - group.number_women},
                ]
            })

        parties = {
            'name': '17. Bundestag',
            'children': children
        }

        context['series'] = json.dumps(series, cls=DjangoJSONEncoder)
        context['years'] = json.dumps(years_list, cls=DjangoJSONEncoder)
        context['values'] = json.dumps(values, cls=DjangoJSONEncoder)
        context['parties'] = json.dumps(parties, cls=DjangoJSONEncoder)
        return context

