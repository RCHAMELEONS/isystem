from django import forms
from .models import Answers


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ['question', 'answer_content', 'image', 'file']


class AnswerFormUpdate(forms.ModelForm):
    class Meta:
        class Meta:
            model = Answers
            fields = ['question', 'answer_content', 'image', 'file']
