from django.forms import ModelForm
from .models import *

class newWebhookForm(ModelForm):
    class Meta:
        model = newWebhhook
        fields = []