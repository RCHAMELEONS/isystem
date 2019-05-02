from django.shortcuts import render
from .forms import QuestionForm, QuestionUpdateForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Questions
from django.urls import reverse_lazy
from users.models import User
from django.shortcuts import redirect
from answers.models import Answers


def index(request):
    questions = []
    answers = []

    for question in Questions.objects.all().order_by('-id'):
        for answer in Answers.objects.all().order_by('-id'):
            if answer.question == question:
                questions.append(question)
                answers.append(answer)
    return render(request, "index_q.html", {'questions': questions, 'answers': answers})


class QuestionCreate(CreateView):
    form_class = QuestionForm
    template_name = "questions_forms/create.html"

    def form_valid(self, form):
        user = User.objects.get(email=self.request.user)
        obj = form.save(commit=False)
        obj.people = user
        obj.save()
        return redirect('questions_index')


class QuestionUpdate(UpdateView):
    template_name = "questions_forms/update.html"
    model = Questions
    form_class = QuestionUpdateForm

    def get_object(self, queryset=None):
        question = Questions.objects.get(id=self.kwargs['pk'])
        return question


class QuestionDelete(DeleteView):
    model = Questions
    template_name = "questions_forms/delete.html"
    success_url = reverse_lazy('questions_index')

