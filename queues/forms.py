from django import forms

from . import choices
from .models import Queue


class QueueCreateForm(forms.ModelForm):
    class Meta:
        model = Queue
        fields = ['queue_number', 'queue_type']

    status = forms.ChoiceField(choices=choices.QueueTypeChoices.choices)