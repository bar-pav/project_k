from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HelloPageView(TemplateView):
    template_name = 'hello.html'