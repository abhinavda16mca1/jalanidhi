from django.conf.urls import url
from django.contrib import admin
from supply import views

urlpatterns = [
	url(r'^reg/',views.reg),
	url(r'^regist/',views.register),
	url(r'^loggs/',views.loggs),
	url(r'^$',views.loggs),
	url(r'^det/',views.reqq),

	
	# url(r'^adminlog/',adminl),
	# url(r'^adminlog/',adminlogg),
	# url(r'^adm/',admin),
	# url(r'^main/',main),
	# url(r'^main/',main),
	# url(r'^update/',update),
	# url(r'^viewstaff/',viewstaff),

]