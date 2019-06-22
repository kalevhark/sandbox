import django
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse(f'Django: {django.get_version()}')