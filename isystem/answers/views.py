from django.shortcuts import render
from .forms import AnswerForm, AnswerFormUpdate
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Answers
from django.urls import reverse_lazy


class AnswerCreate(CreateView):
    form_class = AnswerForm
    template_name = "answer_forms/create.html"


class AnswerUpdate(UpdateView):
    template_name = "questions_forms/update.html"
    model = Answers
    form_class = AnswerFormUpdate

    def get_object(self, queryset=None):
        answer = Answers.objects.get(id=self.kwargs['pk'])
        return answer


class AnswerDelete(DeleteView):
    model = Answers
    template_name = "questions_forms/delete.html"
    success_url = reverse_lazy('index')


