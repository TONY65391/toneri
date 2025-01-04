from django.shortcuts import render
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404,HttpResponse

# Create your views here.

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render(request = request))

def test(request):
    template = loader.get_template('test.html')
    return HttpResponse(template.render(request = request))