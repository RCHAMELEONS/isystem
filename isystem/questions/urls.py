from django.conf.urls import url
from questions.views import QuestionUpdate, QuestionCreate, QuestionDelete
from django.contrib.auth.decorators import login_required
from questions.views import index

urlpatterns = [
    url(r'^$', index, name="questions_index"),
    url(r'^add', login_required(QuestionCreate.as_view()), name="question_add"),
    url(r'^(?P<pk>\d+)/update/$', login_required(QuestionUpdate.as_view()), name="question_update"),
    url(r'^(?P<pk>\d+)/delete/$', login_required(QuestionDelete.as_view()), name="question_delete"),
]
