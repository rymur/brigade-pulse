from django.db import models
from django.utils import timezone


class OverwriteSnapshotException(Exception):
    pass


class TimeSeriesSnapshot(models.Model):
    """
    A TimeSeriesSnapshot is a mixin that automatically records the time a snapshot was taken
    """
    snapshot_time = models.DateTimeField(default=timezone.now())

    def save(self, *args, **kwargs):
        """
        Override save method on TimeSeriesSnapshot to prevent overwriting a snapshot (unless you really meant to!)
        """
        override_behavior = kwargs.pop('override_behavior', False)
        if self.pk and not override_behavior:
            raise OverwriteSnapshotException('You cannot overwrite a TimesSeriesSnapshot instance')
        self.save(*args, **kwargs)

    class Meta(object):
        abstract = True
