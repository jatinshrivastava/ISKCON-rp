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

   
def desired_shloka(request, chapter,shloka_no):
    if shloka_no == 0:
        template = "shloka_index.html"
        #form
        if request.method == 'POST':
            form = ShlokaForm(request.POST)
            chapter = form.data['chapter']
            shloka_no = form.data['shloka_no']
            url = reverse('desired_shloka', kwargs={'chapter':chapter, 'shloka_no':shloka_no})
            return HttpResponseRedirect(url)
        #get_shloka_of_chapter
        shlokas_of_chapter = Shloka.objects.filter(chapter=chapter).order_by('shloka_no')
        context = {
            "chapter": chapter,
            "shlokas_of_chapter": shlokas_of_chapter,
        }
        
    else:
        template = "home.html"
        id = Shloka.objects.filter(Q(chapter=chapter) & Q(shloka_no=shloka_no)).values('id')[0]['id']
        shloka = Shloka.objects.get(id=id)
        #get_chapter_name
        if chapter == 1:
            chapter_name = 'कुरुक्षेत्र के युद्धस्थल में सैन्यनिरीक्षण'
        elif chapter == 2:
            chapter_name = 'गीता का सार'    
        elif chapter == 3:
            chapter_name = 'कर्मयोग'
        elif chapter == 4:
            chapter_name = 'दिव्य ज्ञान'    
        elif chapter == 5:
            chapter_name = 'कर्मयोग - कृष्णभावनाभावित कर्म'
        elif chapter == 6:
            chapter_name = 'ध्यानयोग'
        elif chapter == 7:
            chapter_name = 'भगवद्ज्ञान'
        elif chapter == 8:
            chapter_name = 'भगवत्प्राप्ति'
        elif chapter == 9:
            chapter_name = 'परम गुह्य ज्ञान'
        elif chapter == 10:
            chapter_name = 'श्रीभगवान् का ऐश्वर्य'
        elif chapter == 11:
            chapter_name = 'विराट रूप'
        elif chapter == 12:
            chapter_name = 'भक्तियोग'
        elif chapter == 13:
            chapter_name = 'प्रकृति, पुरुष तथा चेतना'
        elif chapter == 14:
            chapter_name = 'प्रकृति के तीन गुण'
        elif chapter == 15:
            chapter_name = 'पुरुषोत्तम योग'
        elif chapter == 16:
            chapter_name = 'दैवी और आसुरी स्वभाव'
        elif chapter == 17:
            chapter_name = 'श्रद्धा के विभाग'
        else:
            chapter_name = 'उपसंहार - संन्यास की सिद्धि'
        #form
        if request.method == 'POST':
            form = ShlokaForm(request.POST)
            chapter = form.data['chapter']
            shloka_no = form.data['shloka_no']
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
            "chapter_name": chapter_name,
        }
    return render(request, template, context)

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
            url = reverse('desired_shloka', kwargs={'chapter':chapter, 'shloka_no':shloka_no})
            return HttpResponseRedirect(url)
    return render(request, "chapter_index.html")

