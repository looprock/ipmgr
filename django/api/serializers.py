from api.models import ipaddr, ipaddr_dns_name, changelog
from rest_framework import serializers

class ipaddrSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ipaddr
		fields = ('id', 'ipaddress', 'check_dns', 'check_load_balancer', 'check_ping', 'last_update')

class ipaddr_dns_nameSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = ipaddr_dns_name
                fields = ('id', 'ipaddress', 'hostname')

class logSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = changelog
                fields = ('id', 'ipaddress', 'log', 'created')
