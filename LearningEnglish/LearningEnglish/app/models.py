from django.db import models

from django.dispatch import receiver
# Create your models here.
from user.models import UserInfo
from django.db.models.signals import pre_save


class Question(models.Model):
    QUESTION_TYPE = (
        (1, '听力'),
        (2, '阅读理解')
    )
    title = models.TextField(verbose_name='题目', max_length=255, null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='题目创建时间', auto_now_add=True)
    status = models.BooleanField(u'生效', default=True)
    question_type = models.IntegerField(verbose_name='题目类型', choices=QUESTION_TYPE, default=2)

    class Meta:
        verbose_name = "题库题目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Choose(models.Model):
    question = models.ForeignKey(Question, verbose_name='问题', on_delete=models.CASCADE,
                                 related_name='choose_questions')
    option = models.CharField(verbose_name='选项', max_length=150)
    correct_option = models.BooleanField(verbose_name='答案', default=False)

    class Meta:
        verbose_name = "问题选项"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.option


class tingliQuestion(Question):
    class Meta:
        verbose_name = "听力题库"
        verbose_name_plural = verbose_name
        proxy = True


class yueduQuestion(Question):
    class Meta:
        verbose_name = "阅读理解题库"
        verbose_name_plural = verbose_name
        proxy = True

class Answers(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name='用户', on_delete=models.CASCADE, related_name='answers_user_phone')
    question = models.ForeignKey(Question, verbose_name='问题', on_delete=models.CASCADE,
                                 related_name='answers_question_id')
    choose = models.ForeignKey(Choose, verbose_name='问题选项', on_delete=models.CASCADE, null=True, blank=True,
                               related_name='answers_choose')
    create_time = models.DateTimeField(verbose_name='时间', auto_now=True)
    create_data = models.DateField(verbose_name='日期', auto_now=True)
    numbers = models.IntegerField(verbose_name="次数", default=1)
    is_correct = models.BooleanField(verbose_name='是否答对', default=False)
    class Meta:
        verbose_name = "答题记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.question.title)


# @receiver(pre_save, sender=Answers)
# def increment_numbers(sender, instance, **kwargs):
#     if instance.pk:  # 如果是更新操作，递增 numbers 字段
#         instance.numbers += 1
#     else:  # 如果是新建记录，numbers 从 1 开始
#         instance.numbers = 1