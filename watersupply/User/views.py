# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponseRedirect
from datetime import datetime
from models import Complan,userreg

# Create your views here.
def bill(request):
	return render(request,'User/bill.html')
def userlog(request):
	return render(request,'User/userlog.html')	
def complaint(request):
	q=request.session['id']
	print q
	return render(request,'User/details.html',{'ww':q})	
def users(request):
	return render(request,'User/userregister.html')
def reg(request):
	if request.method=="POST":
		Name=request.POST.get('name','')
		Add=request.POST.get('address','')
		Area=request.POST.get('area','')
		Pin=request.POST.get('pin','')
		Phone=request.POST.get('phone','')
		Email=request.POST.get('email','')
		aadhar=request.POST.get('aadhar','')
		Username=request.POST.get('username','')
		Password=request.POST.get('password','')
		cpassword=request.POST.get('cpassword','')
		rr=userreg(Name=Name,Address=Add,Area=Area,Pincode=Pin,Phone=Phone,Email=Email,Aadhar=aadhar,Username=Username,Password=Password,Confirm_Password=cpassword)
		rr.save()
	return HttpResponseRedirect("/User/userlogs")
def login(request):
	if request.method=="POST":
		print "ffffffffffffffffff"
		Username=request.POST.get('Username','')
		Password=request.POST.get('Password','')
		b = userreg.objects.all().filter(Username=Username,Password=Password)
		print b
		if b.exists():
			print "aas"
			for x in b:
				request.session['id']=x.id
					 
			return render(request,'User/userr.html')

		else:
			return render(request,'User/userlog.html',{'qq':'invalid username or password'})	
	return render(request,'User/userlog.html')			
def comp(request):
	print "akjdas"
	if request.method=="POST":
		print "gg"
		r=request.session['id']
		aa=userreg.objects.get(id=r)
		
		# print ee

		# ee=request.POST.get('id','')
		# print ee
		Area=request.POST.get('area','')
		print Area
		Pincode=request.POST.get('pincode','')
		print Pincode
		Complant=request.POST.get('compnt','')
		
		Complaintdes=request.POST.get('complaintdes','')
		print Complaintdes

		dq=Complan(uid=aa,Area=Area,Pincode=Pincode,Complaint=Complant,Complaint_description=Complaintdes)
		dq.save()
	return render(request,'User/compreply.html')
def replycomp(request):
	qw=Complan.objects.all()
	return render(request,'User/compreply.html',{'ww':qw})	
