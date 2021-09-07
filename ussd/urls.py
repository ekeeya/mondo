from django.urls import path
from .views import *

urlpatterns = [
    path('apps', USSDApplicationView.as_view(), name='ussd_apps'),
]
