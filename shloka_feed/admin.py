from django.contrib import admin

from shloka_feed.forms import QuizModelForm
from shloka_feed.models import Shloka, QuizModel, UserAnswerModel
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.db.models import query
from django.contrib.admin.utils import flatten_fieldsets


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
    list_display = ['id', 'chapter', 'shloka_no', 'shloka', 'question']
    radio_fields = {'answer': admin.HORIZONTAL}
    exclude = ()
    fieldsets = (("", {'fields': (
        'chapter', 'shloka_no', 'shloka', 'question', 'optionA', 'optionB', 'optionC', 'optionD', 'answer',
        'point')}),)
    readonly_fields = ('shloka',)

    def save_model(self, request, obj, form, change):
        obj.shloka = Shloka.objects.get(chapter=obj.chapter, shloka_no=obj.shloka_no)
        super().save_model(request, obj, form, change)

    pass


class UserAnswerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'shloka', 'question', 'selected_choice', 'is_correct']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields

        if self.declared_fieldsets:
            return flatten_fieldsets(self.declared_fieldsets)
        else:
            return list(set(
                [field.name for field in self.opts.local_fields] +
                [field.name for field in self.opts.local_many_to_many]
            ))

    pass


admin.site.register(Shloka, ShlokaAdmin)
admin.site.register(QuizModel, QuizModelAdmin)
admin.site.register(UserAnswerModel, UserAnswerModelAdmin)
