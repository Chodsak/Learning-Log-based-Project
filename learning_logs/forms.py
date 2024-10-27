from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%;'})}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        """Limitation of columns"""
        widgets = {'text': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 100%;'})}

