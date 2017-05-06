# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class users(models.Model):
    firstname = models.CharField(max_length=100)
    lastname  = models.CharField(max_length=100)
    