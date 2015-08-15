Django code for ipmgr
======================
a simple api to allow updates of ipaddresses, hostnames, and changelogs

Requires
========

django

django-rest-framework

Howto
=====

Create (minimium):<br>
POST to: api/ipaddrs<br>
{ "ipaddress": "1.1.1.2" }

Update:<br>
POST to: api/ipaddrs/2 <br>
{ "id": 2, "ipaddress": "1.1.1.2", "dns_check": null, "load_balancer_check": null, "ping_test": "True", "last_update": "2015-08-14T20:46:11Z" }

hostnames:

Add:<br>
POST to api/hostnames<br>
{"ipaddress": "1.1.1.2", "hostname": "foo.vast.com"}

Remove:<br>
DELETE to api/hostnames/1

changelogs:

Create:<br>
POST to api/logs<br>
{"ipaddress": "1.1.1.2", "log": "added hostname foo.vast.com"}
