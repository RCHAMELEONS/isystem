from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from users.models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'second_name', 'first_name')
    list_filter = ('is_admin', )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональная информация', {'fields': (
                    'second_name',
                    'first_name',
                    'patronymic',
                    'date_birth',
                    'sex',
                    'phone_number',
                    'email',
                    'nationality',
                    'series_document',
                    'number_document',
                    'date_document',
                    'place_document',
                    'index_registration',
                    'city_registration',
                    'street_registration',
                    'house_registration',
                    'apartment_registration',
                 )}),
        ('Доступ', {'fields': ('is_admin', )})
    )

    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')}),
                ('Персональная информация', {'fields': (
                    'second_name',
                    'first_name',
                    'patronymic',
                    'date_birth',
                    'sex',
                    'phone_number',
                    'email',
                    'nationality',
                    'series_document',
                    'number_document',
                    'date_document',
                    'place_document',
                    'index_registration',
                    'city_registration',
                    'street_registration',
                    'house_registration',
                    'apartment_registration',
                 )}),
                ('Доступ', {'fields': ('is_admin',)})
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)