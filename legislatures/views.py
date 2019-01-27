from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class LegislaturesView(TemplateView):
    template_name = "legislatures/legislatures.html"


