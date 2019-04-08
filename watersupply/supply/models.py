# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class water(models.Model):
	Name = models.CharField(max_length=30,default="")
	address = models.CharField(max_length=30,default="")
	gender =models.CharField(max_length=30,default="")
	dob =models.CharField(max_length=30,default="")
	Username=models.CharField(max_length=30,default="")
	Password =models.CharField(max_length=30,default="")
	Status=models.CharField(max_length=30,default="")
	Username =models.CharField(max_length=30,default="")
	Phoneno =models.CharField(max_length=30,default="")
	Email =models.CharField(max_length=30,default="")
	
