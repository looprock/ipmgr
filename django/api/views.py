import smtplib
import json

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.template import Context, Template, RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser


from api.models import ipaddr, ipaddr_dns_name, changelog
from api.serializers import ipaddrSerializer, ipaddr_dns_nameSerializer, logSerializer

def notify(data):
        print "Notify:"
        print data
	msg_to = "operations@vast.com"
        msg_from = "vmmgr@vast.com"
        server = 'mailrelay.vast.com'
        content = data['log'].split("\n")
        print content
        message = ""
        message += "From: %s\n" % msg_from
        message += "To: %s\n" % msg_to
        message += "Subject: %s: %s\n" % (data['hostname'], content[0])
        message += data['log']
        server = smtplib.SMTP(server)
        server.sendmail(msg_from, msg_to, message)
        server.quit()

# ipaddr
@api_view(['GET', 'POST'])
@csrf_exempt
def ipaddr_api(request):
        if request.method == 'GET':
                ipaddrs = ipaddr.objects.all()
                serializer = ipaddrSerializer(ipaddrs, many=True)
                return Response(serializer.data)
        elif request.method == 'POST':
                serializer = ipaddrSerializer(data=request.DATA)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def ipaddr_api_details(request,pk,format=None):
        if request.method == 'GET':
                ipaddrs = ipaddr.objects.filter(id=pk)
                serializer = ipaddrSerializer(ipaddrs, many=True)
                return Response(serializer.data)
        elif request.method == 'DELETE':
                ipaddrs = ipaddr.objects.filter(id=pk)
                ipaddrs.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'POST':
                ipaddrs = ipaddr.objects.filter(id=pk)[0]
                serializer = ipaddrSerializer(ipaddrs, data=request.DATA, partial=True)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ipaddr_dns_name

@api_view(['GET', 'POST'])
@csrf_exempt
def ipaddr_dns_name_api(request):
    if request.method == 'GET':
        ipaddr_dns_names = ipaddr_dns_name.objects.all()
        serializer = ipaddr_dns_nameSerializer(ipaddr_dns_names, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ipaddr_dns_nameSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
@csrf_exempt
def ipaddr_dns_name_api_details(request,pk,format=None):
    try:
	ipaddr_dns_names = ipaddr_dns_name.objects.filter(id=pk)
    except ipaddr_dns_name.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ipaddr_dns_nameSerializer(ipaddr_dns_names, many=True)
        return Response(serializer.data)
    elif request.method == 'DELETE':
                ipaddr_dns_name.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
# changelogs

@api_view(['GET', 'POST'])
@csrf_exempt
def logs_api(request):
        if request.method == 'GET':
                logs = changelog.objects.all()
                serializer = logSerializer(logs, many=True)
                return Response(serializer.data)
        elif request.method == 'POST':
                serializer = logSerializer(data=request.DATA)
                if serializer.is_valid():
                        serializer.save()
			#notify(request.DATA)
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@csrf_exempt
def logs_api_details(request,pk,format=None):
        logs = changelog.objects.filter(id=pk)
        serializer = logSerializer(logs, many=True)
        return Response(serializer.data)
