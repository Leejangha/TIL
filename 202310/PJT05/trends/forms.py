from django import forms
from .models import Keyword


class KeywordForm(forms.ModelForm):
    input_keywords = forms.CharField(label="키워드", max_length='100')

    class Meta:
        model = Keyword
        fields = ['input_keywords']


class LocationForm(forms.ModelForm):
    input_location = forms.CharField(label="Location", max_length="250")
