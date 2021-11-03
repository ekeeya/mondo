from django import forms
from django.utils.safestring import mark_safe

TYPES = [
    ('', "Select Flow Type"),
    ('ussd', "USSD"),
    ('sms', "SEND SMS"),
    ('email', "SEND EMAIL"),
]

CODES = [
    ('*255#', '*255#'),
    ('*211#', '*211#')
]
TIMEOUTS = [
    ('', 'Timeout after'),
    (300, '5 minutes'),
    (600, '10 minutes'),
    (900, '15 minutes'),
    (600, '30 minutes'),
    (1800, '1 hr'),
    (86400, '1 day'),
    (604800, "A week"),
    ('custom', "Custom")
]


class CreateFlowForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(CreateFlowForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Name"

    name = forms.CharField(
        help_text=mark_safe("<pre style='font-size:8pt;color:#757575'>Get a name that describes this flow, "
                            "e.g. Virtual Banking(*221#)</pre>"),
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "e.g. Virtual Banking (*221#)"
            }
        ))
    type = forms.CharField(
        widget=forms.Select(
            choices=TYPES,
            attrs={
                "class": "form-control select2",
                "style": "width:100%;"
            }
        )
    )
    short_code = forms.CharField(
        widget=forms.Select(
            choices=CODES,
            attrs={
                "class": "form-control select2",
                "style": "width:100%;",
                "multiple": "multiple"
            }
        )
    )
    timeout = forms.CharField(
        widget=forms.Select(
            choices=TIMEOUTS,
            attrs={
                "class": "form-control select2",
                "style": "width:100%;"
            }
        )
    )
