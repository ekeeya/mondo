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
import ast
import uuid

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Flow
import logging

from datetime import datetime

from .forms import CreateFlowForm

logger =  logging.getLogger('main')

class USSDApplicationsListView(TemplateView):
    template_name = "skin/ussd/flows.haml"

    def get(self, request, *args, **kwargs):
        logger.info("THis works")
        form = CreateFlowForm()
        context = dict(form=form)
        return render(request, self.template_name, context)

    def post(self, request):
        pass


class USSDApplicationView(TemplateView):
    template_name = "skin/ussd/flow.haml"

    def get(self, request, *args, **kwargs):
        if 'uuid' in kwargs:
            print(kwargs['uuid'])
        return render(request, self.template_name)


class FlowView(APIView):

    def get(self, request, *args, **kwargs):
        flow_list = [
            dict(id=1, uuid="d5cec018-31b2-4c8a-89d6-6a16093cbb07", name="Test", type='message', archived=False,
                 labels=[],
                 parent_refs=[], expires=100)
        ]
        response = {"results": flow_list}
        return Response(response)


class ActivityView(APIView):

    def get(self, request, *args, **kwargs):
        response = {"nodes": {}, "segments": {}, "recentMessages": {}}
        return Response(response)


class LanguagesView(APIView):
    def get(self, request, *args, **kwargs):
        data = [
            {
                "iso": 'eng',
                "name": 'English'
            }
        ]
        response = {"results": data}
        return Response(response)


class FunctionsView(APIView):
    def get(self, request, *args, **kwargs):
        data = []
        return Response(data)


class RecipientsView(APIView):

    def get(self, request):
        data = [
            {
                'name': 'Cat Fanciers',
                'id': 'eae05fb1-3021-4df2-a443-db8356b953fa',
                'type': 'group',
                'extra': 212
            },
            {
                'name': 'Anne',
                'id': '673fa0f6-dffd-4e7d-bcc1-e5709374354f',
                'type': 'contact'
            }
        ]
        response = {"results": data}
        return Response(response)


class ChannelsView(APIView):

    def get(self, request):
        data = [
            {
                'uuid': '0f661e8b-ea9d-4bd3-9953-d368340acf91',
                'name': 'WhatsApp',
                'address': '+18005234545',
                'schemes': ['whatsapp'],
                'roles': ['send', 'receive']
            }
        ]
        response = {"results": data}
        return Response(response)


class RestHooksView(APIView):

    def get(self, request):
        data = [
            {'resthook': 'my-first-zap', 'subscribers': []},
            {'resthook': 'my-other-zap', 'subscribers': []}
        ]
        response = {"results": data}
        return Response(response)


class TemplatesView(APIView):

    def get(self, request):
        data = []
        response = {"results": data}
        return Response(response)


class EnvironmentView(APIView):
    def get(self, request):
        data = {
            'date_format': 'YYYY-MM-DD',
            'time_format': 'hh:mm',
            'timezone': 'Africa/Kampala',
            'languages': ['eng']
        }
        response = {"results": data}
        return Response(response)


class GroupsView(APIView):
    def get(self, request):
        response = {"results": []}
        return Response(response)


class LabelsView(APIView):

    def get(self, request):
        response = {"results": []}
        return Response(response)

    def post(self, request):
        response = {
            'uuid': uuid.uuid4(),
            'name': "Keeya",
            'count': 0
        }
        return Response(response)


class FieldsView(APIView):

    def get(self, request):
        response = {"results": []}
        return Response(response)


class GlobalsView(APIView):
    def get(self, request):
        response = {"results": []}
        return Response(response)


class ClassifiersView(APIView):

    def get(self, request):
        data = [
            {
                "uuid": '732e4776-dc63-48ad-ae5f-79abd6c462a3',
                "name": 'Travel Agency',
                "type": 'wit',
                "intents": ['book flight', 'rent car'],
                "created_on": '2019-10-15T20:07:58.529130Z'
            }
        ]
        response = {"results": data}
        return Response(response)


class TicketersView(APIView):

    def get(self, request):
        data = [
            {
                "uuid": '5b8587d9-c1bd-47e4-b2ff-dfe790fcdaf2',
                "name": 'Email',
                "type": 'mailgun',
                "created_on": '2019-10-15T20:07:58.529130Z'
            }
        ]
        response = {"results": data}
        return Response(response)


class CompletionView(APIView):

    def get(self, request):
        true = True
        data = {"types": []}
        return Response(data)


class Revisions(APIView):
    def get(self, request, *args, **kwargs):
        print(kwargs)
        flow = None
        if 'uuid' in kwargs:
            uuid = kwargs['uuid']
            revision_list = [{"user": {"email": "chancerton@nyaruka.com", "name": "Chancellor von Frankenbean"},
                              "created_on": "2021-09-08T20:07:30.305Z", "id": 1, "version": "13.0.0", "revision": 1}]
            revisions = dict(
                results=revision_list
            )
        else:
            revision_list = [{"user": {"email": "chancerton@nyaruka.com", "name": "Chancellor von Frankenbean"},
                              "created_on": "2021-09-08T20:07:30.305Z", "id": 1, "version": "13.0.0", "revision": 1}]
            revisions = dict(
                results=revision_list
            )
        return Response(revisions)

    def post(self, request, *args, **kwargs):
        response = {"user": {"email": "chancerton@nyaruka.com", "name": "Chancellor von Frankenbean"},
                    "created_on": "2021-09-08T20:11:08.143Z", "id": 2, "version": "13.0.0", "revision": 2,
                    "metadata": {"issues": []}}
        return Response(response)


class RevisionsView(APIView):

    def get(self, request, *args, **kwargs):
        uuid = None
        if 'uuid' in kwargs:
            uuid = kwargs["uuid"]
        flow_details = dict(
            name="Start",
            language='eng',
            type='ussd',
            spec_version='13.1',
            uuid=uuid,
            localization={},
            nodes=[]
        )
        response = dict(
            definition=flow_details,
            metadata=dict(issues=[])
        )
        return Response(response)
