from django.shortcuts import render
from shloka_feed.models import Shloka
from django.http import HttpResponse, Http404
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView, UpdateView
from .forms import ShlokaForm
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponseRedirect

   
def latest_shloka(request):
    shloka = Shloka.objects.latest('created_on')
    #form
    if request.method == 'POST':
        form = ShlokaForm(request.POST)
        chapter = form.data['chapter']
        shloka_no = form.data['shloka_no']
        id = Shloka.objects.filter(Q(chapter=chapter) & Q(shloka_no=shloka_no)).values('id')[0]['id']
        req_shloka = Shloka.objects.filter(id=id)
        url = reverse('desired_shloka', kwargs={'pshloka':id})
        return HttpResponseRedirect(url)
    #prev_shloka
    prev_shloka_exists = Shloka.objects.filter(id=shloka.id-1).exists()
    if(prev_shloka_exists==True):
        prev_shloka_id = shloka.id-1 
        prev_shloka = Shloka.objects.get(id=prev_shloka_id)
    else:
        prev_shloka = Shloka.objects.get(id=shloka.id)
    #next_shloka
    next_shloka_exists = Shloka.objects.filter(id=shloka.id+1).exists()
    if(next_shloka_exists==True):
        next_shloka_id = shloka.id+1
        next_shloka = Shloka.objects.get(id=next_shloka_id)
    else:
        next_shloka = Shloka.objects.get(id=shloka.id)
    #youtube_embed
    url = shloka.video_url
    url = url.replace("watch?v=", "embed/")
    context = {
        "prev_shloka": prev_shloka,
        "next_shloka": next_shloka,
        "url": url,
        "shloka": shloka,
    }
    return render(request, "home.html", context)

def desired_shloka(request, chapter,shloka_no):
    id = Shloka.objects.filter(Q(chapter=chapter) & Q(shloka_no=shloka_no)).values('id')[0]['id']
    shloka = Shloka.objects.get(id=id)
    #form
    if request.method == 'POST':
        form = ShlokaForm(request.POST)
        chapter = form.data['chapter']
        shloka_no = form.data['shloka_no']
        id = Shloka.objects.filter(Q(chapter=chapter) & Q(shloka_no=shloka_no)).values('id')[0]['id']
        req_shloka = Shloka.objects.filter(id=id)
        url = reverse('desired_shloka', kwargs={'chapter':chapter, 'shloka_no':shloka_no})
        return HttpResponseRedirect(url)
    #prev_shloka
    prev_shloka_exists = Shloka.objects.filter(id=id-1).exists()
    if(prev_shloka_exists==True):
        prev_shloka_id = id-1 
        prev_shloka = Shloka.objects.get(id=prev_shloka_id)
    else:
        prev_shloka = Shloka.objects.get(id=id)
    #next_shloka
    next_shloka_exists = Shloka.objects.filter(id=id+1).exists()
    if(next_shloka_exists==True):
        next_shloka_id = id+1
        next_shloka = Shloka.objects.get(id=next_shloka_id)
    else:
        next_shloka = Shloka.objects.get(id=id)
    #youtube_embed
    url = shloka.video_url
    url = url.replace("watch?v=", "embed/")
    context = {
        "prev_shloka": prev_shloka,
        "next_shloka": next_shloka,
        "url": url,
        "shloka": shloka,
    }
    return render(request, "home.html", context)

def load_shlokas(request):
    chapter_id = request.GET.get('chapter')
    shlokas = Shloka.objects.filter(chapter=chapter_id).order_by('shloka_no')
    return render(request, 'shloka_dropdown_list_options.html', {'shlokas': shlokas})

def chapter_index(request):
    #form
    if request.method == 'POST':
        form = ShlokaForm(request.POST)
        chapter = form.data['chapter']
        shloka_no = form.data['shloka_no']
        id = Shloka.objects.filter(Q(chapter=chapter) & Q(shloka_no=shloka_no)).values('id')[0]['id']
        req_shloka = Shloka.objects.filter(id=id)
        url = reverse('desired_shloka', kwargs={'chapter':chapter, 'shloka_no':shloka_no})
        return HttpResponseRedirect(url)
    #rendering shloka chapters
    shloka = Shloka.objects.all().order_by('-created_on')
    context = {
        "shlokas": shloka,
    }
    return render(request, "chapter_index.html", context)
#def shloka_index(request):
    #shloka = Shloka.objects.all().order_by('-created_on')
    #context = {
        #"shlokas": shloka,
    #}
    #return render(request, "shloka_index.html", context)

#def shloka_detail(request, pshloka):
    #shloka = Shloka.objects.get(pk=pshloka)
    #context = {
        #"shloka": shloka,
    #}

    #return render(request, "shloka_detail.html", context)
