from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader



def index(request):
    return HttpResponse("Hello Django")
