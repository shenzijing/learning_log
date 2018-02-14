"""为应用程序users定义URL模式"""

from django.urls import path,re_path
from django.contrib.auth.views import login

from . import views

app_name = 'users'
urlpatterns = [
	#登录页面
	re_path('^login/$',login,{'template_name':'users/login.html'},
		name='login'),
	#注销
	re_path('^logout/$',views.logout_view,name='logout'),
	#注册页面
	re_path('^register/$',views.register,name='register'),
]
