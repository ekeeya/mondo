from django.urls import path
from .views import *

urlpatterns = [
    path('flows', USSDApplicationsListView.as_view(), name='ussd_apps'),
    path('flow/<str:uuid>', USSDApplicationView.as_view(), name='flow'),
]
