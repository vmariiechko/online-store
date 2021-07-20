from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def helloWorld(request):
    return JsonResponse("Hello World", safe=False)
