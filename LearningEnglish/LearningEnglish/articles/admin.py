from django.contrib import admin

# Register your models here.
from articles.models import Articles


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'title', 'content', 'create_time', 'update_time')
    # list_display_links = ('title',)