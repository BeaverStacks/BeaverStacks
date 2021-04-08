from django.conf.urls import include, url
from django.contrib import admin
from hackathon import views

urlpatterns = [url(r'^$', views.index, name='index'),
    url(r'^hackathon/', include('hackathon.urls')),

    # Changed based on https://stackoverflow.com/questions/43324005/django-deprecation-warning-or-improperlyconfigured-error-passing-a-3-tuple-to
    # It appears this format has changed since the repo was made
    url(r'^admin/', admin.site.urls)]
    