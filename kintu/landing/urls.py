"""
Mondo v 1.0
Created by Keeya Emmanuel  on 01-August-2021

"""

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
]
