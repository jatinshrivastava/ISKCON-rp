from django.contrib import admin
from shloka_feed.models import Shloka
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


admin.site.register(Shloka, ShlokaAdmin)
