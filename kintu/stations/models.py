from django.conf import settings
from django.db import models
from kintu.utils import AuthSignature
from django_countries.fields import CountryField


PLANS = [
    ("f", "Free"),
    ('b', 'Basic'),
    ('p', 'Premium')
]


class Station(AuthSignature):
    name = models.CharField(200)
    plan = models.CharField(
        max_length=10,
        choices=PLANS,
        default=settings.DEFAULT_PLAN
    )
    plan_start = models.DateTimeField(null=True)
    plan_end = models.DateTimeField(null=True)
    timezone = models.CharField(max_length=20)
    metadata = models.TextField(null=True)
    is_deleted = models.BooleanField(default=False)
    country = CountryField(blank_label='(Select Country)')







