from django.shortcuts import render
from shloka_feed.models import Shloka
from django.http import HttpResponse, Http404
from django.http import JsonResponse
from django.views.generic.base import TemplateView




   
def latest_shloka(request):
    shloka = Shloka.objects.latest('created_on')
    context = {
        "shloka": shloka,
    }
    return render(request, "home.html", context)

def desired_shloka(request, chapter, number):
    chapter = Shloka.objects.get(chapter=chapter)
    shloka_number = Shloka.objects.get(number=number)
    required_shloka = chapter & shloka_number
    context = {
        "required_shloka": required_shloka
    }
    return JsonResponse(context)

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