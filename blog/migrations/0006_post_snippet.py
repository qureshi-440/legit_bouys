# Generated by Django 3.1.8 on 2021-05-07 08:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210506_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.TextField(default=datetime.datetime(2021, 5, 7, 8, 41, 55, 671439), max_length=255),
            preserve_default=False,
        ),
    ]