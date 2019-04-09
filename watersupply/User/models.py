# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class userreg(models.Model):

	Name = models.CharField(max_length=30)
	Address = models.CharField(max_length=30)
	Area =models.CharField(max_length=30)
	Pincode=models.CharField(max_length=30)
	Phone =models.CharField(max_length=30)
	Email=models.CharField(max_length=30)
	Aadhar =models.CharField(max_length=30)
	Username =models.CharField(max_length=30)
	Password=models.CharField(max_length=30)
	Confirm_Password=models.CharField(max_length=30)
class Complan(models.Model):
	uid = models.ForeignKey(userreg)
	Area = models.CharField(max_length=30)
	Pincode=models.CharField(max_length=30)
	Complaint=models.CharField(max_length=30)
	Complaint_description =models.CharField(max_length=30)
	Complaint_Reply=models.CharField(max_length=30,default='')	