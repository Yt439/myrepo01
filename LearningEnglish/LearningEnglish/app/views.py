import json

from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.views import View
from gtts import gTTS
# Create your views here.
from django.http import HttpResponse
import os
from django.contrib import messages
from app.models import Question, Answers
from emialApi import sendemial
from user.models import UserInfo
from utils import ApiResponse


def datamp(request):
    # if request.method == 'GET':
    text = request.GET.get('text', 'Hello, world!')
    tts = gTTS(text=text, lang='en')

    mp3_filename = 'output.mp3'
    tts.save(mp3_filename)

    with open(mp3_filename, 'rb') as mp3_file:
        response = HttpResponse(mp3_file.read(), content_type='audio/mp3')
        response['Content-Disposition'] = 'attachment; filename="output.mp3"'

    os.remove(mp3_filename)
    return response


class findQuestionView(View):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        user_id = req_data.get('user_id', None)
        user = UserInfo.objects.get(id=user_id)
        number = Answers.objects.get(user=user).order_by('-id').first()
        if number:
            number_data = number.numbers + 1
        else:
            number_data = 1
        for qs in Question.objects.filter().order_by('?')[:10]:
            Answers.objects.create(question=qs, user=user, numbers=number_data)
        anwers = Answers.objects.filter(user=user, numbers=number_data)
        data = []
        for an in anwers:
            data.append({
                'id': an.id,
                'question': an.question.question,
                'answer': an.question.answer,
                'numbers': an.numbers,
            })
        return ApiResponse.success(data=data)

class upEmail(View):
    def get(self,request):
        user_id = request.GET.get('user_id', None)
        user_data = UserInfo.objects.get(id=user_id)
        days_inactive = (now() - user_data.end_time).days if user_data.end_time else None
        if days_inactive is not None:
            content = f"用户 {user_data.username} 您好,您已经有 {days_inactive} 天没有登录英语学习小程序了，请及时登录。"
        else:
            content = f"用户 {user_data.username}您好，您创建账号后从未登录，请及时登录。"
        sendemial(emial=user_data.email,content=content)
        print('user_id')
        print(user_id)
        messages.success(request, '发送成功')
        return redirect(request.META.get('HTTP_REFERER'))

