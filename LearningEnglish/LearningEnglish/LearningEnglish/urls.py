"""
URL configuration for LearningEnglish project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from LearningEnglish import settings
from app import views as app_views
from user import views as user_views
from base import views as base_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('datamp/', app_views.datamp, name='datamp'),
    path('upEmail/', app_views.upEmail.as_view(), name='upEmail'),
    path('login', user_views.LoginView.as_view(), name='login'),
    path('register', user_views.RegisterView.as_view(), name='register'),
    path('FindUserView', user_views.FindUserView.as_view(), name='FindUserView'),
    path('UpdateUserView', user_views.UpdateUserView.as_view(), name='UpdateUserView'),
    path('upload_avatar', user_views.upload_avatar, name='upload_avatar'),
    path('findThesaurusList', base_views.findThesaurusList.as_view(), name='findThesaurusList'),  # 查找词库
    path('findThesaurusData', base_views.findThesaurusData.as_view(), name='findThesaurusData'),
    path('findArticlesList', base_views.findArticlesList.as_view(), name='findArticlesList'),  # 查找文章
    path('findArticlesData', base_views.findArticlesData.as_view(), name='findArticlesData'),
    path('findAnnouncementList', base_views.findAnnouncementList.as_view(), name='findAnnouncementList'),  # 查找公告
    path('findAnnouncementData', base_views.findAnnouncementData.as_view(), name='findAnnouncementData'),
    path('findPinlunList', base_views.findPinlunList.as_view(), name='findPinlunList'),  # 获取评论
    path('addPinlun', base_views.addPinlun.as_view(), name='addPinlun'),  # 添加评论
    path('findQuestionList', base_views.findQuestionList.as_view(), name='findQuestionList'),  # 获取题库
    path('updateAnswers', base_views.updateAnswers.as_view(), name='updateAnswers'),
    path('select_score', base_views.select_score.as_view(), name='select_score'),  # 答题后获取积分
    path('findpaihang', base_views.findpaihang.as_view(), name='findpaihang'),  # 获取排行榜
    path('findUserdata', base_views.findUserdata.as_view(), name='findUserdata'),  # 获取用户数据
    path('findAnswers', base_views.findAnswers.as_view(), name='findAnswers'),  # 获取答题记录
    path('findAnswersData', base_views.findAnswersData.as_view(), name='findAnswersData'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)