from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse
from .forms import FORMS
from .models import MODELS
from .serializer import SERIALIZER


def test(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request = request))