from django.shortcuts import render
from django.views.generic import ListView
from Marketia.models import Services, ClientLogo
# Create your views here.
from blog.models import Post


# class ServicesList(ListView):
#     model = Services
#     template_name = 'home/index.html'

def home(request):
    posts = Post.objects.all()[:3]
    services = Services.objects.all()
    clients = ClientLogo.objects.all()
    return render(request, 'home/index.html', {
        'posts': posts,
        'services': services,
        'clients': clients
    })


def sitemap(request):
    return render(request, 'home/sitemap.xml')


def robots(request):
    return render(request, 'home/robots.txt')