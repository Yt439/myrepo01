from django.db import models
import uuid


# Create your models here.


class UserInfo(models.Model):
    uuid = models.CharField(verbose_name='用户编号', max_length=255, default=uuid.uuid4)
    username = models.CharField(verbose_name='用户名', max_length=32, null=False, blank=False)
    password = models.CharField(verbose_name='密码', max_length=32, null=False, blank=False)
    email = models.EmailField(verbose_name='邮箱', null=False, blank=False)
    img = models.CharField(verbose_name='头像', max_length=128, null=True, blank=True)
    address = models.CharField(verbose_name='地址', max_length=128, null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    end_time = models.DateTimeField(verbose_name='上次登录时间', auto_now_add=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
