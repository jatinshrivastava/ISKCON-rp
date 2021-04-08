from django import forms
from django.forms import Select

from users.constants import ANSWER_CHOICES
from .models import Shloka, QuizModel


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


class QuizModelForm(forms.ModelForm):
    class Meta:
        model = QuizModel
        fields = '__all__'

    def clean(self):
        cleaned_data = self.cleaned_data
        chapter = cleaned_data.get('chapter')
        shloka_no = cleaned_data.get('shloka_no')
        try:
            shloka_object = Shloka.objects.get(chapter=chapter, shloka_no=shloka_no)
        except:
            raise forms.ValidationError(u"The given shloka number and chapter combination does not exist!")
        return cleaned_data
