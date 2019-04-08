from django.conf.urls import url
from django.contrib import admin
from admin1 import views

urlpatterns = [
	
	
	
	url(r'^$',views.adminlogg),
	url(r'^adm/',views.admin),
	url(r'^main/',views.main),
	url(r'^main/',views.main),
	url(r'^update/',views.update),
	url(r'^viewstaff/',views.viewstaff),

]