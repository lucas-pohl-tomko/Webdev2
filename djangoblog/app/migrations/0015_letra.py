# Generated by Django 2.2.3 on 2019-08-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_document_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Letra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('letra', models.TextField()),
            ],
        ),
    ]
