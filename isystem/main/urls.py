from django.conf.urls import url
from .views import index, contacts, lk
import django.contrib.auth.views as views


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^lk/$', lk, name="lk"),
    url(r'^contacts/$', contacts, name="contacts"),
    url(r'^login/$', views.login, {"template_name": "login.html"}, name="login"),
]
