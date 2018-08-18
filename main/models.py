# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.db import models

# Create your models here.

class DjangoBoard(models.Model):
    subject = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    created_date = models.DateField(default=timezone.now)
    contents = models.CharField(max_length=500, blank=True)

