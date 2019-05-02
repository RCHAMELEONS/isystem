from django.shortcuts import render
from users.models import User
from questions.models import Questions
from appeals.models import Appeals
from answers.models import Answers
from responses.models import Responses


def index(request):
    return render(request, "index.html")


def contacts(request):
    return render(request, "contacts.html")


def lk(request):
    user = str(request.user)

    if(user != 'AnonymousUser'):
        user = User.objects.get(email=request.user)
        questions = Questions.objects.filter(people=user).order_by('-id')
        appeals = Appeals.objects.filter(people=user).order_by('-id')
        answers = Answers.objects.all().order_by('-id')
        responses = Responses.objects.all().order_by('-id')

        return render(request, "lk.html", {'questions': questions, 'appeals': appeals, 'user': user,
                                           'answers': answers, 'responses': responses})
    else:
        return render(request, "login.html")
