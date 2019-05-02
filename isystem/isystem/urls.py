from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from isystem import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^', include("main.urls")),
    url('^questions/', include("questions.urls")),
    url('^answers/', include("answers.urls")),
    url('^user/', include("users.urls")),
    url('^appeals/', include("appeals.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

