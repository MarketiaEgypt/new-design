from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from Marketia.models import Services
# Create your views here.
from blog.models import Post


# class ServicesList(ListView):
#     model = Services
#     template_name = 'home/index.html'

def home(request):
    posts = Post.objects.all()[:3]
    services = Services.objects.all
    return render(request, 'home/index.html', {
        'posts': posts,
        'services': services,
    })


def sitemap(request):
    return reverse(request, 'home/sitemap.xml')


def robots(request):
    return reverse(request, 'home/robots.txt')