from django.conf.urls import url
from django.contrib import admin
from User import views

urlpatterns = [
	url(r'^bill/',views.bill),
	url(r'^users/',views.users),
	url(r'^userlogs/',views.userlog),
	url(r'^login/',views.login),
	url(r'^complaint/',views.complaint),
	url(r'^reg/',views.reg),
	url(r'^comp/',views.comp),
	url(r'^replycomp/',views.replycomp),
	
]	