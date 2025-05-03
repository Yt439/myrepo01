import os
import xml.etree.ElementTree as ET
from datetime import datetime

import django
import uuid
from faker import Faker



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LearningEnglish.settings')
django.setup()

from base.models import *
from articles.models import Articles

from user.models import UserInfo
from app.models import Question, Choose
import random
from community.models import Announcement, Pinlun

fake_en = Faker()
fake_zh = Faker('zh_CN')  # 创建中文 faker 实例


def add_Thesaurus():
    word_roots = ['analy', 'evalu', 'synth', 'quant', 'reli', 'measur', 'inter', 'experi', 'perceiv', 'react']
    types = [1, 2, 3, 4]

    for i in range(50):
        root = random.choice(word_roots)
        suffix = random.choice(['ize', 'ate', 'ify', '', 'ment', 'ing'])
        word = root + suffix

        entry = {
            "word": word,
            "fanyi": fake_zh.word(ext_word_list=["分析", "评估", "合成", "量化", "理解", "观察", "表达", "解释", "测量", "识别"]),
            "type": random.choice(types),
            "liju": fake_en.sentence(nb_words=6),
            "liju_fanyi": fake_zh.sentence(nb_words=6)
        }

        Thesaurus.objects.create(
            word=entry["word"],
            fanyi=entry["fanyi"],
            type=entry["type"],
            liju=entry["liju"],
            liju_fanyi=entry["liju_fanyi"]
        )

    print("50 条词汇数据已成功插入。")


def add_articles():
    for _ in range(20):
        article = Articles(
            uuid=str(uuid.uuid4()),  # 保证每条唯一
            title=fake_en.sentence(nb_words=4),
            title_fanyi=fake_zh.sentence(nb_words=4),
            content=fake_en.paragraph(nb_sentences=5),
            content_fanyi=fake_zh.paragraph(nb_sentences=5)
        )
        article.save()

    print("成功生成 20 条文章数据")


def add_announcements(n=10):
    announcement_data = [
        {"title": "系统维护通知", "content": "为了提供更好的服务体验，平台将于本周六（4月27日）凌晨1:00至5:00进行系统维护，期间将暂停访问，敬请谅解。"},
        {"title": "五一劳动节放假安排", "content": "根据国家法定节假日安排，我平台将于5月1日至5月3日放假三天，5月4日（星期六）正常上班，请大家提前做好安排。"},
        {"title": "关于新增学习打卡功能的公告", "content": "为鼓励大家坚持每日学习，我们新增了“学习打卡”功能，完成每日任务即可获得积分奖励，欢迎积极参与！"},
        {"title": "英语角活动通知", "content": "本周五下午4点将在图书馆多功能厅举行英语角活动，欢迎感兴趣的同学报名参与，提升口语能力。"},
        {"title": "版本更新说明（v2.1.0）", "content": "平台已于今日完成v2.1.0版本更新，优化了界面设计，修复了部分已知问题，欢迎体验新版功能。"},
        {"title": "账号安全提示", "content": "请广大用户定期修改登录密码，开启手机验证码登录，避免账号被盗造成损失。"},
        {"title": "平台使用调查问卷", "content": "为了更好地优化平台，我们推出了用户满意度调查问卷，填写问卷可获得100积分奖励，欢迎反馈宝贵意见！"},
        {"title": "暑期课程报名开放", "content": "2025年暑期线上强化班现已开放报名，课程包括听力、写作与口语专项提升，名额有限，先到先得。"},
        {"title": "积分商城上线啦！", "content": "用户可使用学习积分在积分商城兑换实物奖品、会员时长等福利，快来看看你能兑换什么吧！"},
        {"title": "关于学员成绩统计说明", "content": "期末成绩将于下周统一公布，届时请登录个人中心查看，若有异议请在3日内提交申诉。"}
    ]
    for item in announcement_data:
        Announcement.objects.create(
            title=item["title"],
            content=item["content"]
        )
    print("✅ 成功插入正式公告数据！")


def create_userinfo(n=10):
    for _ in range(n):
        UserInfo.objects.create(
            username=fake_zh.user_name(),
            password=fake_zh.password(length=8),  # 随机密码
            email=fake_zh.email(),
            img=fake_zh.image_url(),  # 随机头像URL
            address=fake_zh.address(),
            end_time=fake_zh.date_this_year(),  # 设置一个随机的上次登录时间
        )
    print(f"✅ 成功生成 {n} 条用户数据")


def create_pinlun(n=30):
    for _ in range(n):
        user_id = random.randint(5, 14)
        announcement_id = random.randint(2, 11)

        try:
            user = UserInfo.objects.get(id=user_id)
            announcement = Announcement.objects.get(id=announcement_id)

            Pinlun.objects.create(
                user=user,
                content=fake_zh.sentence(nb_words=12),
                announcement=announcement
            )
        except UserInfo.DoesNotExist:
            print(f"用户 ID {user_id} 不存在，跳过")
        except Announcement.DoesNotExist:
            print(f"公告 ID {announcement_id} 不存在，跳过")

    print(f"✅ 成功生成 {n} 条评论数据")


def create_questions_with_options(n=30):
    for _ in range(n):
        question_type = random.choice([1, 2])
        title = fake_en.sentence(nb_words=12)

        question = Question.objects.create(
            title=title,
            question_type=question_type,
            status=True
        )

        correct_index = random.randint(0, 3)  # 在4个选项中随机一个为正确答案

        for i in range(4):
            Choose.objects.create(
                question=question,
                option=fake_en.sentence(nb_words=6),
                correct_option=(i == correct_index)
            )

    print(f"✅ 成功生成 {n} 道题目，每题含4个选项")


if __name__ == '__main__':
    # add_Thesaurus()
    # add_articles()
    # add_announcements()
    # create_userinfo()
    create_pinlun()
    # create_questions_with_options()
