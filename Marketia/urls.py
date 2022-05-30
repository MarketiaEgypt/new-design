from django.urls import path

from . import views


app_name = 'Marketia'

urlpatterns = [
    path('', views.home, name='home'),
    path('sitemap.xml/', views.sitemap, name='sitemap'),
    path('robots.txt/', views.robots, name='robots')
]
