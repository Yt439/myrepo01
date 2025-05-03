from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User, Group

from community.models import Announcement, Pinlun

admin.site.unregister(User)
admin.site.unregister(Group)
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date')
    search_fields = ['tilte']
@admin.register(Pinlun)
class PinlunAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'date','announcement')
    search_fields = ['content']
