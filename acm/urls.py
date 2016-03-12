"""acm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from trinity import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    
    url(r'^submit1$',views.answer_submit1,name='answer_submit1'),
    url(r'^submit2$',views.answer_submit2,name='answer_submit2'),
    url(r'^submit3$',views.answer_submit3,name='answer_submit3'),
    url(r'^submit4$',views.answer_submit4,name='answer_submit4'),
    url(r'^submit5$',views.answer_submit5,name='answer_submit5'),
    url(r'^submit6$',views.answer_submit6,name='answer_submit6'),
    url(r'^submit7$',views.answer_submit7,name='answer_submit7'),
    url(r'^submit8$',views.answer_submit8,name='answer_submit8'),
    url(r'^submit9$',views.answer_submit9,name='answer_submit9'),
    url(r'^score$',views.score,name='score'),
    url(r'^$',views.home,name='home'),
    


]
