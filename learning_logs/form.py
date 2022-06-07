from dataclasses import field, fields
from importlib.metadata import files
from pyexpat import model
from django import forms

from .models import Topics

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ['text']
        labels = {'text':""}
        