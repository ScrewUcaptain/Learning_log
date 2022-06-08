from dataclasses import field, fields
from importlib.metadata import files
from pyexpat import model
from django import forms
from matplotlib import widgets

from .models import Topics, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ['text']
        labels = {'text':""}
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': " "}
        widgets = {"text": forms.Textarea(attrs={'cols':80})}
        