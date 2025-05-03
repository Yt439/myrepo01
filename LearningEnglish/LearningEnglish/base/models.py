from django.db import models


# Create your models here.

class Thesaurus(models.Model):
    TYPE_DATA = (
        (1, '雅思词汇'),
        (2, '托福词汇'),
        (3, 'RGE词汇'),
        (4, 'GMAT词汇'),
    )
    word = models.CharField(verbose_name='单词', max_length=20)
    fanyi = models.CharField(verbose_name='翻译', max_length=20)
    type = models.IntegerField(verbose_name='类型', choices=TYPE_DATA)
    liju = models.CharField(verbose_name='例句', max_length=20)
    liju_fanyi = models.CharField(verbose_name='例句翻译', max_length=20)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = '词库'
        verbose_name_plural = verbose_name




