from django.contrib import admin

# Register your models here.
from api.models import ipaddr
from api.models import ipaddr_dns_name
from api.models import changelog

admin.site.register(ipaddr)
admin.site.register(ipaddr_dns_name)
admin.site.register(changelog)
