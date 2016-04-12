from __future__ import unicode_literals
from django.db import models

class Workers(models.Model):
    salary = models.IntegerField()
    hired_on = models.DateField()
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    business = models.ForeignKey('Business', on_delete=models.CASCADE)


class Business(models.Model):
    name = models.CharField(max_length=100)
    employees = models.ManyToManyField(Worker,through=Workers)

class Worker(models.Model):
    name = models.CharField(max_length=100) 