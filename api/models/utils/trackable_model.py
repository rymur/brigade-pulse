from django.db import models


class TrackableModel(models.Model):
    """
    TrackableModel is a mixin that allows us to track the created/updated time on a model
    """
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta(object):
        abstract = True
