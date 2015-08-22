from api.snapshots.django_time_series import DjangoTimeSeries


class BrigadeSnapshot(DjangoTimeSeries):
    @property
    def time_series_properties(self):
        return ['name', 'website', 'events_url']

    @property
    def app_label(self):
        return 'api'

    @property
    def model_name(self):
        return 'brigade'


class ProjectSnapshot(DjangoTimeSeries):
    @property
    def time_series_properties(self):
        return ['name', 'description', 'link_url', 'code_url', 'status', 'tags', 'last_updated']

    @property
    def app_label(self):
        return 'api'

    @property
    def model_name(self):
        return 'project'
