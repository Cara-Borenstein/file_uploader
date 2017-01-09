# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-09 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_to_image', models.CharField(max_length=100, null=True)),
                ('datafile', models.FileField(null=True, upload_to='')),
                ('url', models.URLField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
