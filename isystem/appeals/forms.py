from django import forms
from .models import Appeals


class AppealForm(forms.ModelForm):
    class Meta:
        model = Appeals
        fields = ['people', 'theme', 'content_appeals', 'image', 'file']
        widgets = {'people': forms.HiddenInput()}


class AppealFormUpdate(forms.ModelForm):
    class Meta:
        class Meta:
            model = Appeals
            fields = ['people', 'theme', 'content_appeals', 'image', 'file']
            widgets = {'people': forms.HiddenInput()}
