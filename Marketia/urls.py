from django.urls import path

from . import views


app_name = 'Marketia'

urlpatterns = [
    path('', views.home, name='home'),

]
