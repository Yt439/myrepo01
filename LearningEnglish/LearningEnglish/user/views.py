import datetime
import json

from django.contrib.auth import login
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.models import UserInfo
from utils import ApiResponse


class LoginView(APIView):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        print(req_data)
        # username = req_data.get('username')
        email = req_data.get('email')
        password = req_data.get('password')
        print(email)
        print(password)
        user = UserInfo.objects.filter(email=email, password=password).first()
        if user is not None:
            user.end_time = datetime.datetime.now()
            user.save()
            # 登录用户
            # login(request, user)
            # 返回成功的响应
            context = {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
            return ApiResponse.success(message="登录成功", data=context)
        return ApiResponse.error(message="用户名或密码错误")

class RegisterView(APIView):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        username = req_data.get('username')
        password = req_data.get('password')
        email = req_data.get('email')
        user = UserInfo.objects.filter(username=username).first()
        if user is not None:
            return ApiResponse.error(message="用户名已存在")
        user = UserInfo.objects.create(username=username, password=password, email=email)
        # 登录用户
        # login(request, user)
        # 返回成功的响应
        context = {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
        return ApiResponse.success(message="注册成功", data=context)


class FindUserView(APIView):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        user_id = req_data.get('user_id')
        user = UserInfo.objects.filter(id=user_id).first()
        if user is not None:
            context = {
                "id": user.id,
                "username": user.username,
                "img": user.img,
                "email": user.email,
                "address": user.address,
                "create_time": user.create_time,
                "end_time": user.end_time,
            }
            return ApiResponse.success(data=context)
        return ApiResponse.error(message="用户名不存在")

class UpdateUserView(APIView):
    def post(self, request):
        if request.body:
            req_data = json.loads(request.body)
        else:
            req_data = {}
        user_id = req_data.get('user_id')
        username = req_data.get('username')
        address = req_data.get('address')
        password = req_data.get('password')
        email = req_data.get('email')
        user = UserInfo.objects.filter(id=user_id).first()
        if user is not None:
            user.username = username
            user.address = address
            user.password = password
            user.email = email
            user.save()
            context = {
                "id": user.id,
                "username": user.username,
                "img": user.img,
                "email": user.email,
                "address": user.address,
                "create_time": user.create_time,
                "end_time": user.end_time,
            }
            return ApiResponse.success(data=context)
        return ApiResponse.error(message="用户名不存在")

def upload_avatar(request):
    if request.method == 'POST' and request.FILES['avatar']:
        user_id = request.POST.get('user_id')
        user = UserInfo.objects.get(id=user_id)  # 获取用户实例

        avatar_file = request.FILES['avatar']
        fs = FileSystemStorage()

        # 为图片命名并保存
        avatar_name = f'{user_id}_{avatar_file.name}'
        avatar_path = fs.save(f'avatars/{avatar_name}', avatar_file)
        avatar_url = fs.url(avatar_path)

        # 更新用户的头像 URL
        user.img = avatar_url
        user.save()

        # 返回上传后的头像 URL
        return JsonResponse({'success': True, 'avatarUrl': avatar_url})

    return JsonResponse({'success': False, 'message': '头像上传失败'})
