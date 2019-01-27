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
        data =  [legislature.percentage for legislature in legislatures]

        result = []

        for legislature in legislatures:

            result.append({
                'name': legislature.name,
                'year': legislature.year,
                'percentage': legislature.percentage,
            })



        context['legislatures'] = json.dumps(data, cls=DjangoJSONEncoder)
        context['years'] = json.dumps(years, cls=DjangoJSONEncoder)
        return context

