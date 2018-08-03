# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-03 08:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('a_id', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('abstract', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('second_category', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='post')),
                ('tag', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.User')),
            ],
            options={
                'db_table': 'article_tb',
            },
        ),
    ]