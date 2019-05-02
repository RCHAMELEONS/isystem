from django.conf.urls import url
from answers.views import AnswerCreate, AnswerUpdate, AnswerDelete
from django.contrib.auth.decorators import login_required
from questions.views import index

urlpatterns = [
    url(r'^$', index, name="questions_index"),
    url(r'^add', login_required(AnswerCreate.as_view()), name="answer_add"),
    url(r'^(?P<pk>\d+)/update/$', login_required(AnswerUpdate.as_view()), name="answer_update"),
    url(r'^(?P<pk>\d+)/delete/$', login_required(AnswerDelete.as_view()), name="answer_delete"),
]
