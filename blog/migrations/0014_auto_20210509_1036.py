# Generated by Django 3.1.8 on 2021-05-09 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20210508_1038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-time']},
        ),
    ]
