from django.conf.urls import url
from users.views import UserRegister, UserUpdate, UserDelete


urlpatterns = [
    url(r'^register', UserRegister.as_view(), name="user_register"),
    url(r'^update', UserUpdate.as_view(), name="user_update"),
]
