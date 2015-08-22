from django.db import models

from api.models import GitHubUser
from api.models.utils.trackable_model import TrackableModel


class GitHubRepository(TrackableModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    contributors = models.ManyToManyField(GitHubUser, through='GitHubRepositoryContributor')
    owner = models.ForeignKey(GitHubUser, related_name='my_repos')
    homepage = models.URLField(max_length=1000, null=True, blank=True)

    stargazers_count = models.IntegerField()
    watchers_count = models.IntegerField()
    forks_count = models.IntegerField()
    open_issues = models.IntegerField()

    created_at = models.DateTimeField()

    class Meta(object):
        db_table = 'github_repository'
        app_label = 'api'


class GitHubRepositoryContributor(TrackableModel):
    repository = models.ForeignKey(GitHubRepository)
    contributor = models.ForeignKey(GitHubUser)
    contributions = models.PositiveIntegerField()

    class Meta(object):
        db_table = 'github_repo_contributors'
        app_label = 'api'
