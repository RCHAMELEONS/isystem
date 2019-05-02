from django import forms
from .models import Questions


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['people', 'theme', 'content_question', 'image', 'file']
        widgets = {'people': forms.HiddenInput()}


class QuestionUpdateForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['people', 'theme', 'content_question', 'image', 'file']
        widgets = {'people': forms.HiddenInput()}
