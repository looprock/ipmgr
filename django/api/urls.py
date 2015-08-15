from django.conf.urls import patterns, url
from rest_framework import routers, serializers, viewsets
from api import views

urlpatterns = patterns('',
	url(r'^api/ipaddrs$', views.ipaddr_api, name='ipaddr_api'),
	url(r'^api/ipaddrs/(?P<pk>[0-9]+)/$', views.ipaddr_api_details, name='ipaddr_api_details'),
        url(r'^api/hostnames$', views.ipaddr_dns_name_api, name='ipaddr_dns_name_api'),
        url(r'^api/hostnames/(?P<pk>[0-9]+)/$', views.ipaddr_dns_name_api_details, name='ipaddr_dns_name_api_details'),
        url(r'^api/logs$', views.logs_api, name='logs_api'),
        url(r'^api/logs/(?P<pk>[0-9]+)/$', views.logs_api_details, name='logs_api_details')
)
