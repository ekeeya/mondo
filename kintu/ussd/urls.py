from django.urls import path
from .views import *

urlpatterns = [
    path('flows', USSDApplicationsListView.as_view(), name='ussd_apps'),
    path('flow/<str:uuid>', USSDApplicationView.as_view(), name='flow'),
    path('activity', ActivityView.as_view(), name='activity'),
    path('languages/', LanguagesView.as_view(), name='languages'),
    path('groups', GroupsView.as_view(), name='groups'),
    path('labels/', LabelsView.as_view(), name='labels'),
    path('fields/', FieldsView.as_view(), name='fields'),
    path('globals/', GlobalsView.as_view(), name='globals'),
    path('ticketers/', TicketersView.as_view(), name='ticketers'),
    path('classifiers/', ClassifiersView.as_view(), name='classifiers'),
    path('functions/', FunctionsView.as_view(), name='functions'),
    path('recipients/', RecipientsView.as_view(), name='recipients'),
    path('channels/', ChannelsView.as_view(), name='channels'),
    path('resthooks/', RestHooksView.as_view(), name='resthooks'),
    path('templates/', TemplatesView.as_view(), name='templates'),
    path('flows/', FlowView.as_view(), name='flows'),
    path('environment/', EnvironmentView.as_view(), name='environment'),
    path('completion/', CompletionView.as_view(), name='completion'),
    path('revisions/<str:uuid>/<int:revision_id>', RevisionsView.as_view()),
    path('revisions/<str:uuid>/', Revisions.as_view()),
    path('revisions/', Revisions.as_view()),
    path('revisions1/', Revisions.as_view()),
]
