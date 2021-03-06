"""SSL URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from SSL import settings
from . import views


urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^a/$', views.webmail, name='webmail'),
    url(r'^accounts/profile/$', views.index,name='index'),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/profile/user/$', views.edit_profile, name='user'),
    url(r'^accounts/profile/table/$', views.teaching, name='table'),
    url(r'^accounts/profile/publication/$', views.publication, name='publication'),
    url(r'^accounts/profile/projects/$', views.projects, name='projects'),
    url(r'^accounts/profile/achievements/$', views.achievements, name='achievements'),
    url(r'^accounts/profile/education/$', views.education, name='education'),
    url(r'^signup/$', views.signup, name='editprofile'),
    url(r'^accounts/profile/table/delete/(?P<part_id>[0-9]+)/$', views.function, name='delete_view'),
    url(r'^accounts/profile/publication/delete/(?P<part_id>[0-9]+)/$', views.function2, name='delete_view2'),
    url(r'^accounts/profile/education/delete/(?P<part_id>[0-9]+)/$', views.function3, name='delete_view3'),
    url(r'^accounts/profile/projects/delete/(?P<part_id>[0-9]+)/$', views.function4, name='delete_view4'),
    url(r'^accounts/profile/achievements/delete/(?P<part_id>[0-9]+)/$', views.function5, name='delete_view5'),

    url(r'^profile/(?P<username>.+)/$', views.show_main, name='show'),
    url(r'^search/$', views.find_user_by_name, name='search1'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)