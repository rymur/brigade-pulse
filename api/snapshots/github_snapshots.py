from api.snapshots.django_time_series import DjangoTimeSeries


class GitHubRepositorySnapshot(DjangoTimeSeries):
    @property
    def time_series_properties(self):
        return ['name', 'description', 'language', 'homepage', 'stargazers_count', 'watchers_count', 'forks_count',
                'open_issues']

    @property
    def app_label(self):
        return 'api'

    @property
    def model_name(self):
        return 'githubrepository'


class GitHubContributorSnapshot(DjangoTimeSeries):
    @property
    def time_series_properties(self):
        return ['contributions']

    @property
    def app_label(self):
        return 'api'

    @property
    def model_name(self):
        return 'githubrepositorycontributor'
