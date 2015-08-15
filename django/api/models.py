from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class ipaddr(models.Model):
	ipaddress = models.GenericIPAddressField()
	check_dns = models.NullBooleanField()
	check_load_balancer = models.NullBooleanField()
	check_ping = models.NullBooleanField()
	last_update = models.DateTimeField(auto_now_add=True, blank=True)
	def __unicode__(self):
		return 'ipaddress: %s, check_dns: %s, check_load_balancer: %s, check_ping: %s, last_update: %s' % (self.ipaddress, str(self.check_dns), str(self.check_load_balancer), str(self.check_ping), self.last_update)

class ipaddr_dns_name(models.Model):
        ipaddress = models.GenericIPAddressField()
	hostname = models.CharField(max_length=512)
        def __unicode__(self):
                return 'ipaddress: %s, hostname: %s' % (self.ipaddress, self.hostname)

class changelog(models.Model):
	ipaddress = models.GenericIPAddressField()
	log = models.TextField()
	created = models.DateTimeField(auto_now_add=True, blank=True)
	def __unicode__(self):
		return 'ipaddress: %s, log: %s, date: %s' % (self.ipaddress, self.log, self.created)
