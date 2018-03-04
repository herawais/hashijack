from django.db import models


class Data(models.Model):
    date = models.DateField()
    tag = models.CharField(max_length=15, default='')
