from django.conf.urls import url
from django.contrib import admin
from supply import views

urlpatterns = [
	url(r'^reg/',views.reg),
	url(r'^regist/',views.register),
	url(r'^loggs/',views.loggs),
	
	

]