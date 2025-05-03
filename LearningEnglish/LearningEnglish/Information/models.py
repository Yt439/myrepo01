from django.db import models

# Create your models here.
from user.models import UserInfo


class Information(models.Model):
    user = models.ForeignKey(verbose_name='催发用户', to=UserInfo, on_delete=models.CASCADE, related_name='information_user', null=True)
    title = models.CharField(verbose_name='信息标题', max_length=100, null=True)
    content = models.TextField(verbose_name='信息内容', max_length=1000, null=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '催发信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
