# Generated by Django 2.2.3 on 2019-08-06 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190806_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='follower',
        ),
    ]
