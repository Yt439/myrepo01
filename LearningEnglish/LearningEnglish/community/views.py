import json

from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views import View

from community.models import Announcement, Pinlun
from user.models import UserInfo
from utils import ApiResponse


class findAnnouncementViewList(View):
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
            return Announcement.error(message="没有更多了")
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


class findAnnouncementViewData(View):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        title = req_data.get('title', None)
        id = req_data.get('id', None)
        query = Q()
        if title:
            query &= Q(title__icontains=title)
        if id:
            query &= Q(id=id)
        result = Announcement.objects.filter(query).first()
        if not result:
            return ApiResponse.error(message="没有更多了")
        data = {}
        data['id'] = result.id
        data['title'] = result.title
        data['content'] = result.content
        data['date'] = result.date
        result_count = Announcement.objects.filter(query).count()
        result_data = {
            "data": data,
            "total": result_count
        }
        return ApiResponse.success(data=result_data)


class findPinlunViewList(View):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        ann_id = req_data.get('ann_id', None)
        currentPage = req_data.get('currentPage', 1)
        pageSize = req_data.get('pageSize', 20)
        query = Q()
        if ann_id:
            ann_one = Announcement.objects.get(id=ann_id)
            query &= Q(announcement=ann_one)
        result = Pinlun.objects.filter(query)[currentPage * pageSize - pageSize:currentPage * pageSize]
        if not result:
            return ApiResponse.error(message="没有更多了")
        result_data = []
        for i in result:
            data = {}
            data['id'] = i.id
            data['content'] = i.content
            data['user'] = i.user.username
            data['date'] = i.date
            result_data.append(data)
        result_count = Announcement.objects.filter(query).count()
        result_data = {
            "data": result_data,
            "total": result_count
        }
        return ApiResponse.success(data=result_data)


class addPinlunViewData(View):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        ann_id = req_data.get('ann_id', None)
        user_id = req_data.get('user_id', None)
        content = req_data.get('content', None)
        if ann_id:
            ann_one = Announcement.objects.get(id=ann_id)
        if user_id:
            user_one = UserInfo.objects.get(id=user_id)
        Pinlun.objects.create(announcement=ann_one, user=user_one, content=content)
        return ApiResponse.success(msg="评论成功")
