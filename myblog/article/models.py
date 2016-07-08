from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
    pos_id = models.BigIntegerField()
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)