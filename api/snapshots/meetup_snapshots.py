from api.snapshots.django_time_series import DjangoTimeSeries


class MeetupEventSnapshot(DjangoTimeSeries):
    @property
    def time_series_properties(self):
        return ['yes_rsvp_count', 'maybe_rsvp_count', 'waitlist_count', 'headcount']

    @property
    def app_label(self):
        return 'api'

    @property
    def model_name(self):
        return 'meetupevent'


class MeetupGroupSnapshot(DjangoTimeSeries):
    @property
    def time_series_properties(self):
        return ['organizer_name', 'topics', 'rating', 'members']

    @property
    def app_label(self):
        return 'api'

    @property
    def model_name(self):
        return 'meetupgroup'
