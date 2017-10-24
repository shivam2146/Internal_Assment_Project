"""is URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from students.views import mainpage 
from django.contrib.auth import views as auth_views
from students import views as is_view
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',mainpage),
    url(r'^teacher/$',is_view.teahome),
    url(r'^tea1/(?P<sid>\w{0,50})/$',is_view.teahome1),
    url(r'^tea2/upd/(?P<sid>\w{0,50})/(?P<subid>\w{0,50})/$',is_view.teahome2),
    url(r'^logredi/$',is_view.logred),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}),
    url(r'^signup/$', is_view.signup, name='signup'),
    url(r'', include('students.urls')),
    url(r'^signup/stu_signup/$',is_view.stu_sign),
    url(r'^signup/tea_signup/$',is_view.tea_sign),
   
   

]
