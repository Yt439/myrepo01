# Generated by Django 4.2.19 on 2025-02-26 08:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_articles_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='uuid',
            field=models.CharField(default=uuid.UUID('69a38564-347f-4554-a77f-da0766e8e4cf'), max_length=255, verbose_name='文章编号'),
        ),
    ]
