from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views
from django.conf import settings

urlpatterns = [
    path("", views.latest_shloka, name='latest_shloka'),
    path("ch=<int:chapter>/no=<int:number>", views.desired_shloka, name='desired_shloka'),
  ]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()