from django.contrib import admin

# Register your models here.

from .models import *


# 听力题库
@admin.register(tingliQuestion)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_time', 'question_type')

    def get_queryset(self, request):
        queryset = super().get_queryset(request).filter(question_type=1)
        return queryset


# 阅读理解题库
@admin.register(yueduQuestion)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_time', 'question_type')

    def get_queryset(self, request):
        queryset = super().get_queryset(request).filter(question_type=2)
        return queryset


@admin.register(Choose)
class ChooseAdmin(admin.ModelAdmin):
    list_display = ('question', 'option', 'correct_option')
