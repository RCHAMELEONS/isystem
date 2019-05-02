from django.conf.urls import url
from appeals.views import AppealCreate, AppealUpdate, AppealDelete
from django.contrib.auth.decorators import login_required
from questions.views import index

urlpatterns = [
    url(r'^$', index, name="appeals_index"),
    url(r'^add', login_required(AppealCreate.as_view()), name="appeal_add"),
    url(r'^(?P<pk>\d+)/update/$', login_required(AppealUpdate.as_view()), name="appeal_update"),
    url(r'^(?P<pk>\d+)/delete/$', login_required(AppealDelete.as_view()), name="appeal_delete"),
]
