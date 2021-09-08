from django import forms
from django.utils.safestring import mark_safe

TYPES = [
    ('', "SELECT FLOW TYPE"),
    ('ussd', "USSD"),
    ('sms', "SEND SMS"),
    ('email', "SEND EMAIL"),
]

CODES = [
    ('*255#', '*255#'),
    ('*211#', '*211#')
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
                "style": "width:200px;"
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
