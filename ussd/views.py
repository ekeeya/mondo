"""
Copyright (C) 2021 Digital Solutions

This software has been initially thought through and developed by Keeya Emmanuel <ekeeya@ds.co.ug> for digital solutions

Part of this software is free fro usage on github.
Purchase your licence to get the full power of this software.
contact us on

dev@mondo.io
sale@mondo.io
ekeeya@mondo.io

"""

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class USSDApplicationsListView(TemplateView):
    template_name = "skin/ussd/flows.haml"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class USSDApplicationView(TemplateView):
    template_name = "skin/ussd/flow.haml"

    def get(self, request, *args, **kwargs):
        if 'uuid' in kwargs:
            print(kwargs['uuid'])
        return render(request, self.template_name)
