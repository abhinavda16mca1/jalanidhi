# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponseRedirect

from models import adminlog
from supply.models import water
from User.models import Complan,userreg

# Create your views here.
def adminlogg(request):	
	if request.method=="POST":
		Username=request.POST.get('username','')
		print Username
		Password=request.POST.get('password','')

		pp = adminlog.objects.all().filter(Username=Username,Password=Password)

		if pp.exists():
			return render(request,'admin/main.html')
		else:
			return render(request,'admin/ad.html',{'qq':'invalid'})

	return render(request,'admin/ad.html')
		
def admin(request):
	reg = water.objects.all().filter(Status=0)
	print reg
	return render(request,'admin/adm.html',{"rr":reg})

def main(request):
	return render(request,'admin/main.html')

def update(request):
	c=request.GET.get('id','')
	k=water.objects.all().filter(id=c).update(Status=1)
	print k
	return HttpResponseRedirect("/admin/adm")
def viewstaff(request):

	view=water.objects.all().filter(Status=1)
	return render(request,'admin/viewstaff.html',{"rr":view})
	return HttpResponseRedirect("/admin/viewstaff")
def approvecomp(request):
	
	ii = request.session["id"]
	print ii
	qq=Complan.objects.select_related('uid').filter(Complaint_Reply='')
	print qq
	

	return render(request,'admin/approvecomp.html',{"cc":qq})
def reply(request):
	if request.method=="POST":
		id=request.POST.get('idd')
		Reply = request.POST.get('rep','')
		print Reply
		# qm=Complan(Complaint_Reply=Reply)
		Complan.objects.filter(id=id).update(Complaint_Reply=Reply)
		return HttpResponseRedirect("/admin/approvecomp")
		# qm.save()

	q=request.GET.get('id','')
	aa=Complan.objects.all().filter(id=q)
	return render(request,'admin/adminreply.html',{"ee":aa})
# def replycompl(request):
	




