from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views
from django.conf import settings

urlpatterns = [
    path("", views.chapter_index, name='chapter_index'),
    #path("ch=<int:pchapter>/no=<int:number>", views.next_shloka, name='next_shloka'),
    path("<int:chapter>/<int:shloka_no>", views.desired_shloka, name='desired_shloka'),
    path('ajax/load_shlokas/', views.load_shlokas, name='ajax_load_shlokas'),
  ]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()