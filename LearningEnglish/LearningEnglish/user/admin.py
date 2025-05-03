from django.contrib import admin, messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import path
from django.utils.html import format_html
from emialApi import sendemial
from user.models import UserInfo

admin.site.site_header = '英语词汇学习系统管理平台'
admin.site.site_title = '英语词汇学习系统管理平台'
admin.site.index_title = '英语词汇学习系统管理平台'

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'username', 'email', 'address', 'create_time', 'end_time', 'remind_online_button')
    search_fields = ['username']

    def remind_online_button(self, obj):
        return format_html(
            '<a class="el-button el-button--plain el-button--small" href="{}">提醒上线</a>',
            f"/upEmail?user_id={obj.id}"
        )

    remind_online_button.short_description = '提醒上线'

