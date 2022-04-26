from django.urls import path
from .views import ServicesList


app_name = 'Marketia'

urlpatterns = [
    path('', ServicesList.as_view(), name='services_list'),

]
