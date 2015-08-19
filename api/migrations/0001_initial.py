# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brigade',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('started_on', models.DateField(null=True, blank=True)),
                ('website', models.URLField(max_length=1000)),
                ('type', models.CharField(max_length=255)),
                ('events_url', models.URLField(max_length=1000)),
                ('rss', models.URLField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GitHubRepository',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('language', models.CharField(max_length=255, null=True, blank=True)),
                ('contributors', models.BooleanField()),
                ('owner', models.BooleanField()),
                ('homepage', models.URLField(max_length=1000, null=True, blank=True)),
                ('stargazers_count', models.IntegerField()),
                ('watchers_count', models.IntegerField()),
                ('forks_count', models.IntegerField()),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MeetupEvent',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('location', models.CharField(max_length=255, null=True, blank=True)),
                ('organization_name', models.CharField(max_length=255)),
                ('event_url', models.URLField(max_length=1000)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True, blank=True)),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('link_url', models.URLField(max_length=1000, null=True, blank=True)),
                ('code_url', models.URLField(max_length=1000, null=True, blank=True)),
                ('status', models.CharField(max_length=255, null=True, blank=True)),
                ('tags', models.TextField(null=True, blank=True)),
                ('organization_name', models.CharField(max_length=255)),
                ('last_updated', models.DateTimeField(null=True, blank=True)),
                ('brigade', models.ForeignKey(to='api.Brigade')),
                ('github_repository', models.ForeignKey(blank=True, to='api.GitHubRepository', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
