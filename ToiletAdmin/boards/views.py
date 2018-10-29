# from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello, World!')


def tuPutaMadre(request):
    return HttpResponse("<div><strong>TU puta madre!</strong><div/>"
                        "<br>")
