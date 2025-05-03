from django.db import models
import uuid


# Create your models here.

class Articles(models.Model):
    uuid = models.CharField(verbose_name='文章编号', max_length=255, default=uuid.uuid4())
    title = models.CharField(verbose_name='文章标题', max_length=100, null=True, blank=True)
    title_fanyi = models.CharField(verbose_name='文章标题翻译', max_length=100, null=True, blank=True)
    content = models.TextField(verbose_name='文章内容', max_length=100, null=True, blank=True)
    content_fanyi = models.TextField(verbose_name='文章内容翻译', null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now_add=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title


