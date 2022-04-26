from django.shortcuts import render
from django.views.generic import ListView
from Marketia.models import Services
# Create your views here.


class ServicesList(ListView):
    model = Services
    template_name = 'index.html'
