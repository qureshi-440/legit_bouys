# Generated by Django 3.1.8 on 2021-05-08 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
    ]