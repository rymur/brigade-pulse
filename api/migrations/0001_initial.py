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
                'db_table': 'brigade',
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
                ('homepage', models.URLField(max_length=1000, null=True, blank=True)),
                ('stargazers_count', models.IntegerField()),
                ('watchers_count', models.IntegerField()),
                ('forks_count', models.IntegerField()),
                ('open_issues', models.IntegerField()),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'github_repository',
            },
        ),
        migrations.CreateModel(
            name='GitHubRepositoryContributor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('contributions', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'github_repo_contributors',
            },
        ),
        migrations.CreateModel(
            name='GitHubUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('avatar_url', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'github_user',
            },
        ),
        migrations.CreateModel(
            name='MeetupEvent',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('venue_name', models.CharField(max_length=255, null=True, blank=True)),
                ('group_name', models.CharField(max_length=255)),
                ('event_url', models.URLField(max_length=1000)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True, blank=True)),
                ('yes_rsvp_count', models.PositiveIntegerField(default=0)),
                ('maybe_rsvp_count', models.PositiveIntegerField(default=0)),
                ('waitlist_count', models.PositiveIntegerField(default=0)),
                ('headcount', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField()),
                ('brigade', models.ForeignKey(to='api.Brigade')),
            ],
            options={
                'db_table': 'meetup_event',
            },
        ),
        migrations.CreateModel(
            name='MeetupGroup',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('organizer_name', models.CharField(max_length=255)),
                ('topics', models.TextField(null=True, blank=True)),
                ('rating', models.FloatField(null=True, blank=True)),
                ('members', models.PositiveIntegerField()),
                ('brigade', models.ForeignKey(to='api.Brigade')),
            ],
            options={
                'db_table': 'meetup_group',
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
                'db_table': 'project',
            },
        ),
        migrations.AddField(
            model_name='githubrepositorycontributor',
            name='contributor',
            field=models.ForeignKey(to='api.GitHubUser'),
        ),
        migrations.AddField(
            model_name='githubrepositorycontributor',
            name='repository',
            field=models.ForeignKey(to='api.GitHubRepository'),
        ),
        migrations.AddField(
            model_name='githubrepository',
            name='contributors',
            field=models.ManyToManyField(to='api.GitHubUser', through='api.GitHubRepositoryContributor'),
        ),
        migrations.AddField(
            model_name='githubrepository',
            name='owner',
            field=models.ForeignKey(related_name='my_repos', to='api.GitHubUser'),
        ),
    ]
