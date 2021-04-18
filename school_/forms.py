
from django import forms
from .models import Class_Madrese


class SchoolForm(forms.ModelForm):

    class Meta:
        model = Class_Madrese
        fields = ['title', 'name', 'body', 'image']