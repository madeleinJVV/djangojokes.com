from django.shortcuts import render
from django.views.generic import TemplateView
import templates
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'