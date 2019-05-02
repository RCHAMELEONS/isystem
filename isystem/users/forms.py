from django import forms
from .models import User


class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['second_name', 'first_name', 'patronymic', 'date_birth', 'sex', 'phone_number', 'email',
                  'nationality', 'series_document', 'number_document', 'date_document', 'place_document',
                  'index_registration', 'city_registration', 'street_registration', 'house_registration',
                  'apartment_registration']

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return password2

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['second_name', 'first_name', 'patronymic', 'date_birth', 'sex', 'phone_number', 'email',
                  'nationality', 'series_document', 'number_document', 'date_document', 'place_document',
                  'index_registration', 'city_registration', 'street_registration', 'house_registration',
                  'apartment_registration']
