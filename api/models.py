from django.db import models

# Create your models here.


class Brigade(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField('api.Person')


class Person(models.Model):
    name = models.CharField(max_length=255)