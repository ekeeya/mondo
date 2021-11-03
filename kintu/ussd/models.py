from django.db import models
from kintu.utils import AuthSignature
import uuid

FLOW_TYPE = [
    ("USSD", "USSD"),
    ("OTHER", "OTHER")
]

APP_LABEL = 'flows'


class Flow(AuthSignature):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    name = models.CharField(
        max_length=70,
        help_text="The country this organization should map results for."
    )
    is_active = models.BooleanField(
        default=True
    )
    is_deleted = models.BooleanField(
        default=False
    )
    flow_type = models.CharField(
        max_length=10,
        choices=FLOW_TYPE,
        default="USSD"
    )
    expires_after_minutes = models.IntegerField(
        default=30,
        help_text="After these minutes, a contact will restart the flow from the entry node"
    )

    class Meta:
        app_label = APP_LABEL
