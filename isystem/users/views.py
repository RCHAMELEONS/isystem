from django.shortcuts import render
from .forms import UserForm, UserUpdateForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import User
from django.urls import reverse_lazy


class UserRegister(CreateView):
    form_class = UserForm
    add_form = UserForm
    template_name = "user_forms/create.html"


class UserUpdate(UpdateView):
    template_name = "user_forms/update.html"
    model = User
    form_class = UserUpdateForm

    def get_object(self, queryset=None):
        user = User.objects.get(email=self.request.user)
        return user


class UserDelete(DeleteView):
    model = User
    template_name = "user_forms/delete.html"
    success_url = reverse_lazy('index')


