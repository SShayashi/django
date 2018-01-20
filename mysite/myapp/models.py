from django.db import models


class Bar(models.Model):
    pass


class Foo(models.Model):
    bar = models.ManyToManyField('Foo', blank=True)
