# Generated by Django 2.2.3 on 2019-08-06 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190806_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='relationships',
            field=models.ManyToManyField(blank=True, related_name='related_to', through='app.Follow', to='app.Profile'),
        ),
    ]