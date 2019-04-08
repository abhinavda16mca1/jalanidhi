# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponseRedirect

from models import water

# Create your views here.
def reg(request):
	return render(request,'staff/staff.html')
def register(request):
	print "cdsfvdbbg"
	Name=request.POST.get('name','')
	address=request.POST.get('adr','')
	gender=request.POST.get('rd','')
	dob=request.POST.get('dob','')
	
	print "ak"
	Username=request.POST.get('user','')
	Password=request.POST.get('pass','')
	Email=request.POST.get('email','')
	Phone=request.POST.get('phone','')
	
	a = water(Name=Name,address=address,gender=gender,dob=dob,Username=Username,Password=Password,Status=0,Email=Email,Phoneno=Phone)
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
					return render(request,'staff/details.html')
		else:
			return render(request,'staff/login.html',{'qq':'invalid username or password'})	
	return render(request,'staff/login.html')
	
def reqq(request):
	return render(request,'staff/details.html')	
	

		 





