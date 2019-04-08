# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class adminlog(models.Model):
	Username =models.CharField(max_length=30)
	Password =models.CharField(max_length=30)	