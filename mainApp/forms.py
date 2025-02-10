from django import forms
from .models import *

class UstozForm(forms.ModelForm):
    class Meta:
        model = Ustoz
        fields = "__all__"
class YonalishForm(forms.ModelForm):
    class Meta:
        model = Yonalish
        fields = "__all__"
class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = "__all__"

