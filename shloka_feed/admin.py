from django.contrib import admin
from shloka_feed.models import Shloka


class ShlokaAdmin(admin.ModelAdmin):
    list_display = ['id','chapter','shloka_no','shloka']
    pass

admin.site.register(Shloka, ShlokaAdmin)
