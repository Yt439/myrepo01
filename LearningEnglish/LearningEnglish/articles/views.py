import json

from django.db.models import Q
from django.shortcuts import render
from app.ApiResponse import *

# Create your views here.
from django.views import View

from articles.models import Articles
from base.models import Thesaurus
from utils import ApiResponse


class findArticlesViewList(View):
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
        result = Articles.objects.filter(query)[currentPage * pageSize - pageSize:currentPage * pageSize]
        if not result:
            return ApiResponse.error(message="没有更多了")
        result_data = []
        for i in result:
            data = {}
            data['id'] = i.id
            data['title'] = i.title
            data['content'] = i.content
            result_data.append(data)
        result_count = Articles.objects.filter(query).count()
        result_data = {
            "data": result_data,
            "total": result_count
        }
        return ApiResponse.success(data=result_data)


class findArticlesViewData(View):
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
        result = Articles.objects.filter(query).first()
        if not result:
            return ApiResponse.error(message="没有更多了")
        data = {}
        data['id'] = result.id
        data['title'] = result.title
        data['title_fanyi'] = result.title_fanyi
        data['content'] = result.content
        data['content_fanyi'] = result.content_fanyi
        result_count = Articles.objects.filter(query).count()
        result_data = {
            "data": data,
            "total": result_count
        }
        return ApiResponse.success(data=result_data)
