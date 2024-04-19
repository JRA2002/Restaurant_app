from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomView(TemplateView):
    template_name = "Restlima/home.html"