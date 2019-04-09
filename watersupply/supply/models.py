# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class water(models.Model):
	Name = models.CharField(max_length=30)
	Desig = models.CharField(max_length=30)
	Department =models.CharField(max_length=30)
	Username=models.CharField(max_length=30)
	Password =models.CharField(max_length=30)
	Status=models.CharField(max_length=30)
	Username =models.CharField(max_length=30)
	Phoneno =models.CharField(max_length=30)
	Email =models.CharField(max_length=30)

