import django
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        'django_version': f'Django: {django.get_version()}',
        'request': request.META
    }
    # return HttpResponse(f'Django: {django.get_version()}')
    return render(
        request,
        'home/home.html',
        context
    )