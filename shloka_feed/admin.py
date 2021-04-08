from django.contrib import admin

from shloka_feed.forms import QuizModelForm
from shloka_feed.models import Shloka, QuizModel
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.db.models import query

# from shloka_feed.models import Profile
#
#
# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'profile'


# Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (ProfileInline,)


# Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)


class ShlokaAdmin(admin.ModelAdmin):
    list_display = ['id', 'chapter', 'shloka_no', 'shloka']
    pass


class QuizModelAdmin(admin.ModelAdmin):
    form = QuizModelForm
    list_display = ['id', 'chapter', 'shloka_no', 'shloka_id', 'question']
    radio_fields = {'answer': admin.HORIZONTAL}
    exclude = ()
    fieldsets = (("", {'fields': (
    'chapter', 'shloka_no', 'shloka_id', 'question', 'optionA', 'optionB', 'optionC', 'optionD', 'answer', 'point')}),)
    readonly_fields = ('shloka_id',)

    def save_model(self, request, obj, form, change):
        obj.shloka_id = Shloka.objects.get(chapter=obj.chapter, shloka_no=obj.shloka_no)
        super().save_model(request, obj, form, change)
    pass


admin.site.register(Shloka, ShlokaAdmin)
admin.site.register(QuizModel, QuizModelAdmin)
