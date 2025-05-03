from django.contrib import admin

# Register your models here.
from base.models import Thesaurus


@admin.register(Thesaurus)
class ThesaurusAdmin(admin.ModelAdmin):
    list_display = ('word', 'fanyi', 'type', 'liju', 'liju_fanyi')
    list_filter = ['type']
    search_fields = ['word']

    # search_fields = ['word', 'type']
    # def has_add_permission(self, request):
    #     return False

