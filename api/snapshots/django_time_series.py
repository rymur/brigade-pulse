from abc import ABCMeta, abstractproperty

from django.db import models, ProgrammingError
from django.db.models.loading import get_model
from django.utils import timezone


class DjangoTimeSeries(object):
    """
    Class to dynamically create time series tables for models where we want to track numerical data for them.
    Supports naming specific fields to capture from the tracked model, as well as defining new fields and tying
    methods to them to populate them in the snapshot (for instance, you might have Project with a FK to Brigade,
    and we might want to save 'project_count' on our Brigade snapshot.  You can do this with tying functions to
    new fields).
    """

    __metaclass__ = ABCMeta

    def __init__(self):
        self.TimeSeriesBaseModel = get_model(self.app_label, self.model_name)
        # first check to see if the model exists in Django's model cache
        from django.apps import registry
        try:
            if registry.apps.get_model(self.app_label, self.name):
                self.TimeSeriesModel = registry.apps.get_model(self.app_label, self.name)
                return
        except LookupError:
            pass

        # model did not exist in Django's model cache, so let's build it and load it
        class Meta:
            db_table = self.name  # TODO support overriding table name

        fields = {
            'original_model': models.ForeignKey(self.TimeSeriesBaseModel),
            'timestamp': models.DateTimeField(db_index=True),
            '__module__': self.app_label + '.models',
            'Meta': Meta
        }
        for f in self.time_series_properties:
            if f == 'timestamp':
                raise Exception('Cannot time series a field named "timestamp"')
            field_class = None
            max_digits = 0
            decimal_places = 0
            max_length = 0
            for model_field in self.TimeSeriesBaseModel._meta.fields:
                if model_field.name == f:
                    field_class = model_field.__class__
                    # TODO support all default django fields
                    if not (issubclass(field_class, models.DecimalField) or
                                issubclass(field_class, models.IntegerField) or
                                issubclass(field_class, models.CharField) or
                                issubclass(field_class, models.TextField) or
                                issubclass(field_class, models.URLField) or
                                issubclass(field_class, models.DateTimeField) or
                                issubclass(field_class, models.DateField) or
                                issubclass(field_class, models.FloatField)):
                        raise Exception("Class {} not supported".format(field_class.__name__))
                    if field_class == models.DecimalField:
                        # must bring over params in the case of decimal field
                        max_digits = model_field.max_digits
                        decimal_places = model_field.decimal_places
                    if field_class == models.CharField:
                        # must bring over max length in case of char field
                        max_length = model_field.max_length
                    break
            if field_class is None:
                raise Exception("Field {} could not be found in class {}".format(f, self.TimeSeriesBaseModel.__name__))
            fields[f] = field_class()
            if field_class == models.DecimalField:
                fields[f].max_digits = max_digits
                fields[f].decimal_places = decimal_places
            if field_class == models.CharField:
                fields[f].max_length = max_length
        for field_name, field_instance, function in self.time_series_functions:
            fields[field_name] = field_instance
        self.TimeSeriesModel = type(self.name, (models.Model,), fields)

        # next make sure that the tables exist in the database.  if not, build them.
        from django.db import connection
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM {} LIMIT 1".format(self.name))
        except ProgrammingError:
            # Looks like the table doesn't exist!  Let's build it!
            from django.db import connection
            from django.db.backends.base.schema import BaseDatabaseSchemaEditor
            schema_editor = BaseDatabaseSchemaEditor(connection)
            with schema_editor:
                schema_editor.create_model(self.TimeSeriesModel)
                # TODO I wonder if I can implement non-destructive altering?

    @property
    def name(self):
        return self.model_name + "_time_series"

    @abstractproperty
    def app_label(self):
        """
        The name of the application for the model we want to time series track
        :return:
        """

    @abstractproperty
    def model_name(self):
        """
        The name of the model the original numbers are stored in
        :return:
        """

    @property
    def time_series_properties(self):
        """
        A list of property names of the model that we want to record time-series rows for
        :return:
        """
        return []

    @property
    def time_series_functions(self):
        """
        A list of tuples (field_name, field_model, function_pointer) that we want to record time-series rows for.  The
        function provided must take a single argument (an instance of the model).  The field_model is an instance of a
        Field subclass (something like models.IntegerField() )
        :return:
        """
        return []

    def create_snapshot(self, original, time=None):
        if not time:
            time = timezone.now()
        time_series_dict = {'timestamp': time,
                            'original_model_id': original.pk}
        for p in self.time_series_properties:
            time_series_dict[p] = getattr(original, p) if getattr(original, p) is not None else 0
        for field_name, _, function in self.time_series_functions:
            time_series_dict[field_name] = function(original)
        self.TimeSeriesModel(**time_series_dict).save()
