# Generated by Django 2.1.7 on 2019-02-28 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0006_auto_20190227_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorganization',
            name='course_number',
            field=models.IntegerField(default=0, verbose_name='课程数量'),
        ),
        migrations.AddField(
            model_name='courseorganization',
            name='students',
            field=models.IntegerField(default=0, verbose_name='学习人数'),
        ),
    ]
