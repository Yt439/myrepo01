# Generated by Django 4.2.19 on 2025-02-26 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_userinfo_uuid'),
        ('community', '0002_auto_20250124_0358'),
    ]

    operations = [
        migrations.CreateModel(
            name='pinlun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, max_length=255, null=True, verbose_name='评论内容')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('announcement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='community.announcement', verbose_name='所属公告')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pinlun_user', to='user.userinfo', verbose_name='发表用户')),
            ],
        ),
    ]
