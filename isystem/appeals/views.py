from django.shortcuts import render
from .forms import AppealForm, AppealFormUpdate
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Appeals
from django.urls import reverse_lazy
from django.shortcuts import redirect
from users.models import User


class AppealCreate(CreateView):
    form_class = AppealForm
    template_name = "appeals_forms/create.html"

    def form_valid(self, form):
        user = User.objects.get(email=self.request.user)
        obj = form.save(commit=False)
        obj.people = user
        obj.save()
        return redirect('/')


class AppealUpdate(UpdateView):
    template_name = "appeals_forms/update.html"
    model = Appeals
    form_class = AppealFormUpdate

    def get_object(self, queryset=None):
        appeal = Appeals.objects.get(id=self.kwargs['pk'])
        return appeal


class AppealDelete(DeleteView):
    model = Appeals
    template_name = "appeals_forms/delete.html"
    success_url = reverse_lazy('index')


