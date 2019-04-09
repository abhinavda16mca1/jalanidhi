# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponseRedirect

from models import water
from datetime import datetime

# Create your views here.
def reg(request):
	return render(request,'staff/staff.html')
def register(request):
	print "cdsfvdbbg"
	Name=request.POST.get('name','')
	Desig=request.POST.get('desig','')
	Department=request.POST.get('dept','')
	print "ak"
	Username=request.POST.get('user','')
	Password=request.POST.get('pass','')
	Email=request.POST.get('email','')
	Phone=request.POST.get('phone','')
	
	a = water(Name=Name,Desig=Desig,Department=Department,Username=Username,Password=Password,Status=0,Email=Email,Phoneno=Phone)
	a.save()
	return HttpResponseRedirect("/supply/loggs")
def loggs(request):
	if request.method=="POST":
		print "ffffffffffffffffff"
		Username=request.POST.get('Username','')
		Password=request.POST.get('Password','')
		b = water.objects.all().filter(Username=Username,Password=Password)
		if b.exists():
			for x in b:
				if x.Status == '0':
					return render(request,'staff/login.html',{'qq':'Not approved'})
				else:

					 
					return render(request,'staff/inside.html')

		else:
			return render(request,'staff/login.html',{'qq':'invalid username or password'})	
	return render(request,'staff/login.html')
	





		 





