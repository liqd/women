import json

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import Legislature

class LegislaturesView(TemplateView):
    template_name = "legislatures/legislatures.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        legislatures = Legislature.objects.all()

        years = [legislature.year for legislature in legislatures]
        types = Legislature.POLITICAL_SYSTEM_CHOICES

        series = []

        for type, typename in types:
            legislatures = Legislature.objects.filter(system=type)
            data = []
            for year in years:
                if legislatures.filter(year=year):
                    #for l in legislatures.filter(year=year):
                    #    data.append(l.percentage)
                    data.append(legislatures.filter(year=year).first().percentage)
                else:
                    data.append('')
            series.append({
                'name': typename,
                'data': data
            })

        context['series'] = json.dumps(series, cls=DjangoJSONEncoder)
        context['years'] = json.dumps(years, cls=DjangoJSONEncoder)
        return context

