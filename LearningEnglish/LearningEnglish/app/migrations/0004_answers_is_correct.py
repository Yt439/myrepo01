# Generated by Django 4.2.19 on 2025-04-24 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='is_correct',
            field=models.BooleanField(default=False, verbose_name='是否答对'),
        ),
    ]
