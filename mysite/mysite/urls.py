#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from books import views 

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', views.index),
    (r'^search/$', views.search),
    (r'^xiangxi/p1(\d+)/$',views.zhanshi),
    (r'^delete/p1(\d+)p2(\d+)/$',views.dele),
    (r'^update/p1(\d+)p2(\d+)/$',views.update),
    (r'^append/$', views.append),
    (r'^appauthor/p1(\d+)/$',views.appauthor),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
