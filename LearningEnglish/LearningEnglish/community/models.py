from django.db import models

# Create your models here.
from user.models import UserInfo


class Announcement(models.Model):
    title = models.CharField(verbose_name='公告标题', max_length=100)
    content = models.TextField(verbose_name='公告信息')
    date = models.DateTimeField(verbose_name='时间', auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '社区公告'
        verbose_name_plural = verbose_name


class Pinlun(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name='发表用户', on_delete=models.CASCADE,
                             related_name='pinlun_user', blank=True, null=True)
    content = models.TextField(verbose_name='评论内容', max_length=255, blank=True, null=True)
    date = models.DateTimeField(verbose_name='发表时间', auto_now_add=True)
    announcement = models.ForeignKey(Announcement, verbose_name='所属公告', on_delete=models.CASCADE, blank=True, null=True)

    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name


