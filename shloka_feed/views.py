from django.shortcuts import render
from shloka_feed.models import Shloka
from django.http import HttpResponse, Http404
from django.http import JsonResponse
from django.views.generic.base import TemplateView

   
def latest_shloka(request):
    shloka = Shloka.objects.latest('created_on')
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

def desired_shloka(request, pshloka):
    shloka = Shloka.objects.get(id=pshloka)
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
