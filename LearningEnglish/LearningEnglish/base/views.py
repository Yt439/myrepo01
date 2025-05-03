from django.core import serializers
from django.db.models import Q, Case, When
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.db.models import Sum, F, Count, IntegerField

from app.models import Answers, Question, Choose
from articles.models import Articles
from base.models import Thesaurus
from community.models import Announcement, Pinlun
from user.models import UserInfo
from utils import ApiResponse
import json


# utils/time_format.py
def format_datetime(dt):
    return dt.strftime('%Y-%m-%d %H:%M') if dt else ''


class findThesaurusList(View):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        type = req_data.get('type', None)
        currentPage = req_data.get('currentPage', 1)
        pageSize = req_data.get('pageSize', 20)
        query = Q()
        if type:
            query &= Q(type=type)
        result = Thesaurus.objects.filter(query)[currentPage * pageSize - pageSize:currentPage * pageSize]
        if not result:
            return ApiResponse.error(message="没有更多了")
        result_data = []
        for i in result:
            data = {}
            data['id'] = i.id
            data['word'] = i.word
            data['fanyi'] = i.fanyi
            data['type'] = i.type
            data['liju'] = i.liju
            data['liju_fanyi'] = i.liju_fanyi
            result_data.append(data)
        result_count = Thesaurus.objects.filter(query).count()
        result_data = {
            "data": result_data,
            "total": result_count
        }
        return ApiResponse.success(data=result_data)


class findThesaurusData(View):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        type = req_data.get('type', None)
        id = req_data.get('id', None)
        query = Q()
        if id:
            query &= Q(id=id)
        if type:
            query &= Q(type=type)

        result = Thesaurus.objects.filter(query).first()
        if not result:
            return ApiResponse.error(message="没有更多了")

        # 获取下一个 ID（当前类型、ID 更大的记录）
        next_thesaurus = Thesaurus.objects.filter(
            Q(type=result.type),
            Q(id__gt=result.id)
        ).order_by('id').first()
        next_id = next_thesaurus.id if next_thesaurus else None

        # 获取上一个 ID（当前类型、ID 更小的记录）
        prev_thesaurus = Thesaurus.objects.filter(
            Q(type=result.type),
            Q(id__lt=result.id)
        ).order_by('-id').first()
        prev_id = prev_thesaurus.id if prev_thesaurus else None

        data = {
            'id': result.id,
            'word': result.word,
            'fanyi': result.fanyi,
            'type': result.type,
            'liju': result.liju,
            'liju_fanyi': result.liju_fanyi,
            'next_id': next_id,
            'prev_id': prev_id
        }

        result_count = Thesaurus.objects.filter(Q(type=result.type)).count()

        result_data = {
            "data": data,
            "total": result_count
        }

        return ApiResponse.success(data=result_data)



class findArticlesList(View):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        title_fanyi = req_data.get('title_fanyi', None)
        currentPage = req_data.get('currentPage', 1)
        pageSize = req_data.get('pageSize', 20)
        query = Q()
        if title_fanyi:
            query &= Q(title_fanyi__icontains=title_fanyi)
        result = Articles.objects.filter(query)[currentPage * pageSize - pageSize:currentPage * pageSize]
        if not result:
            return ApiResponse.error(message="没有更多了")
        result_data = []
        for i in result:
            data = {}
            data['id'] = i.id
            data['uuid'] = i.uuid
            data['title'] = i.title
            data['title_fanyi'] = i.title_fanyi
            data['content'] = i.content
            data['content_fanyi'] = i.content_fanyi
            data['create_time'] = format_datetime(i.create_time)
            result_data.append(data)
        result_count = Articles.objects.filter(query).count()
        result_data = {
            "data": result_data,
            "total": result_count
        }
        return ApiResponse.success(data=result_data)


class findArticlesData(View):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        title_fanyi = req_data.get('title_fanyi', None)
        id = req_data.get('id', None)
        query = Q()
        if id:
            query &= Q(id=id)
        if title_fanyi:
            query &= Q(title_fanyi__icontains=title_fanyi)
        result = Articles.objects.filter(query).first()
        if not result:
            return ApiResponse.error(message="没有更多了")

        # 获取下一个 ID（按当前 query 条件筛选，且 ID 大于当前 ID）
        next_thesaurus = Articles.objects.filter(Q(id__gt=result.id)).order_by('id').first()
        next_id = next_thesaurus.id if next_thesaurus else None

        data = {
            'id': result.id,
            'uuid': result.uuid,
            'title': result.title,
            'title_fanyi': result.title_fanyi,
            'content': result.content,
            'content_fanyi': result.content_fanyi,
            'create_time': format_datetime(result.create_time),
            'next_id': next_id  # 新增字段
        }

        result_count = Articles.objects.filter(Q(title_fanyi__icontains=result.title_fanyi)).count()

        result_data = {
            "data": data,
            "total": result_count
        }

        return ApiResponse.success(data=result_data)


class findAnnouncementList(View):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        title = req_data.get('title', None)
        currentPage = req_data.get('currentPage', 1)
        pageSize = req_data.get('pageSize', 20)
        query = Q()
        if title:
            query &= Q(title__icontains=title)
        result = Announcement.objects.filter(query)[currentPage * pageSize - pageSize:currentPage * pageSize]
        if not result:
            return ApiResponse.error(message="没有更多了")
        result_data = []
        for i in result:
            data = {}
            data['id'] = i.id
            data['title'] = i.title
            data['content'] = i.content
            data['date'] = i.date
            result_data.append(data)
        result_count = Announcement.objects.filter(query).count()
        result_data = {
            "data": result_data,
            "total": result_count
        }
        return ApiResponse.success(data=result_data)


class findAnnouncementData(View):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        title = req_data.get('title', None)
        id = req_data.get('id', None)
        query = Q()
        if id:
            query &= Q(id=id)
        if title:
            query &= Q(title__icontains=title)
        result = Announcement.objects.filter(query).first()
        if not result:
            return ApiResponse.error(message="没有更多了")

        # 获取下一个 ID（按当前 query 条件筛选，且 ID 大于当前 ID）
        next_thesaurus = Announcement.objects.filter(Q(id__gt=result.id)).order_by('id').first()
        next_id = next_thesaurus.id if next_thesaurus else None

        data = {
            'id': result.id,
            'title': result.title,
            'content': result.content,
            'date': result.date,
            'next_id': next_id  # 新增字段
        }

        result_count = Announcement.objects.filter(Q(title__icontains=result.title)).count()

        result_data = {
            "data": data,
            "total": result_count
        }

        return ApiResponse.success(data=result_data)


class findPinlunList(View):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        announcement = req_data.get('announcement', None)
        print('==============')
        print(announcement)
        currentPage = req_data.get('currentPage', 1)
        pageSize = req_data.get('pageSize', 20)
        query = Q()
        if announcement:
            ann_data = Announcement.objects.get(id=announcement)
            query &= Q(announcement=ann_data)
        result = Pinlun.objects.filter(query).order_by('-id')[currentPage * pageSize - pageSize:currentPage * pageSize]
        if not result:
            return ApiResponse.error(message="没有更多了")
        result_data = []
        for i in result:
            data = {}
            data['id'] = i.id
            data['user'] = i.user.username
            data['content'] = i.content
            data['img'] = i.user.img
            data['date'] = i.date
            data['announcement'] = i.announcement.title
            result_data.append(data)
        result_count = Pinlun.objects.filter(query).count()
        result_data = {
            "data": result_data,
            "total": result_count
        }
        return ApiResponse.success(data=result_data)


class addPinlun(View):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        user_id = req_data.get('user_id', None)
        announcement = req_data.get('announcement', None)
        content = req_data.get('content', None)
        user_data = UserInfo.objects.get(id=user_id)
        ann_data = Announcement.objects.get(id=announcement)
        Pinlun.objects.create(
            user=user_data,
            content=content,
            announcement=ann_data
        )
        result_data = {
            "data": "评论成功"
        }
        return ApiResponse.success(data=result_data)

class findQuestionList(View):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        print(req_data)
        user_id = req_data.get('user_id', None)
        user_data = UserInfo.objects.get(id=user_id)
        an_count = Answers.objects.filter(user=user_data).count()
        this_count = (an_count / 10) + 1
        for qs in Question.objects.filter().order_by('?')[:10]:
            Answers.objects.create(
                user=user_data,
                question=qs,
                numbers=this_count,
            )
        answer = Answers.objects.filter(
            user=user_data,
            numbers=this_count
        )
        if not answer:
            return ApiResponse.error(message="没有更多了")
        result_data = []
        for i in answer:
            data = {}
            option = []
            data['id'] = i.id
            data['question'] = i.question.title
            for j in i.question.choose_questions.all():
                option_data = {}
                option_data['option'] = j.option
                option_data['id'] = j.id
                option_data['correct_option'] = j.correct_option
                option.append(option_data)
            data['choose'] = option
            data['create_time'] = format_datetime(i.create_time)
            data['create_data'] = format_datetime(i.create_data)
            data['numbers'] = i.numbers
            result_data.append(data)
        result_data = {
            "data": result_data,
            "number":this_count
        }
        return ApiResponse.success(data=result_data)


class updateAnswers(View):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        choose_id = req_data.get('choose_id', None)
        answer_id = req_data.get('answer_id', None)
        choose_data = Choose.objects.get(id=choose_id)
        Answers_data = Answers.objects.get(id=answer_id)
        Answers_data.choose = choose_data
        Answers_data.is_correct = choose_data.correct_option
        Answers_data.save()
        result_data = {
            "data": Answers_data.is_correct
        }
        return ApiResponse.success(data=result_data)


class select_score(View):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        print(req_data)
        user_id = req_data.get('user_id', None)
        number = req_data.get('number', None)
        user_data = UserInfo.objects.get(id=user_id)
        yes_count = Answers.objects.filter(user=user_data, numbers=number, is_correct=True).count()
        no_count = 10 - yes_count
        result_data = {
            "data": {
                "yes_count": yes_count,
                "no_count": no_count
            }
        }
        return ApiResponse.success(data=result_data)


class findpaihang(View):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        user_scores = (
            Answers.objects
                .filter(is_correct=True)  # 只计算答对的题目
                .values('user')  # 按 user 分组
                .annotate(
                total_score=Count('id')  # 每个答对的记录计 1 分
            )
                .order_by('-total_score')  # 按分数降序排序
        )
        result_data = []
        for user_score in user_scores:
            user_data = UserInfo.objects.get(id=user_score['user'])
            result_data.append({
                "username": user_data.username,
                "score": user_score['total_score'],
                "img": user_data.img,
                "end_time": format_datetime(user_data.end_time),
                "create_time":format_datetime(user_data.create_time),
                "Answers_count": Answers.objects.filter(user=user_data).count()
            })

        result_data = {
            "data": result_data
        }
        return ApiResponse.success(data=result_data)


class findUserdata(View):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        user_id = req_data.get('user_id', None)
        user_data = UserInfo.objects.get(id=user_id)
        Answers_count = Answers.objects.filter(user=user_data).count()
        score = Answers.objects.filter(user=user_data, is_correct=True).count()
        result_data = {
            "username": user_data.username,
            "create_time": format_datetime(user_data.create_time),
            "end_time": format_datetime(user_data.end_time),
            "score": score,
            "Answers_count": Answers_count
        }
        return ApiResponse.success(data=result_data)


class findAnswers(View):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        user_id = req_data.get('user_id', None)
        user_data = UserInfo.objects.get(id=user_id)
        Answers_data = Answers.objects.filter(user=user_data)
        grouped_scores = (
            Answers_data
                .values('numbers')
                .annotate(
                total_score=Sum(
                    Case(
                        When(is_correct=True, then=1),
                        default=0,
                        output_field=IntegerField()
                    )
                ),
                total_records=Count('id')
            )
                .order_by('-numbers')
        )

        if not grouped_scores:
            return ApiResponse.error(message="没有更多了")
        result_data = []
        for i in grouped_scores:
            data = {}
            data['numbers'] = i['numbers']
            data['total_score'] = i['total_score']
            data['total_records'] = i['total_records']
            result_data.append(data)
        result_data = {
            "data": result_data
        }
        return ApiResponse.success(data=result_data)

class findAnswersData(View):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        user_id = req_data.get('user_id', None)
        numbers = req_data.get('numbers', None)
        user_data = UserInfo.objects.get(id=user_id)
        Answers_data = Answers.objects.filter(user=user_data, numbers=numbers)
        if not Answers_data:
            return ApiResponse.error(message="没有更多了")
        result_data = []
        for i in Answers_data:
            data = {}
            data['id'] = i.id
            data['question'] = i.question.title
            if i.choose:
                data['user_choose'] = i.choose.id
            data['create_time'] = format_datetime(i.create_time)
            data['create_data'] = format_datetime(i.create_data)
            data['numbers'] = i.numbers
            data['is_correct'] = i.is_correct
            option = []
            for j in i.question.choose_questions.all():
                option_data = {}
                option_data['option'] = j.option
                option_data['id'] = j.id
                option_data['correct_option'] = j.correct_option
                option.append(option_data)
            data['choose'] = option
            result_data.append(data)
        result_data = {
            "data": result_data
        }
        return ApiResponse.success(data=result_data)