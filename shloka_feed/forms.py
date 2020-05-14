from django import forms
from django.forms import Select
from .models import Shloka

class ShlokaForm(forms.Form):
    chapter = forms.CharField()
    shloka_no = forms.CharField()
    '''class Meta:
        model = Shloka
        fields = ('chapter', 'shloka_no')
        widgets = {
            'chapter': Select(choices=[
    (chapter, chapter) for chapter in Shloka.objects.all()]),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['shloka_no'].queryset = Shloka.objects.none()

        if 'chapter' in self.data:
            try:
                chapter_id = int(self.data.get('chapter'))
                self.fields['shloka_no'].queryset = Shloka.objects.filter(chapter=chapter_id).order_by('shloka_no')
            except (ValueError, TypeError, KeyError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset'''
        