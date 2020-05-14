from django import forms
from .models import *


class profile(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = ('location', 'Age')
