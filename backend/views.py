from django.shortcuts import render
from django.http import JsonResponse


def helloWorld(request):
    return JsonResponse("Hello World", safe=False)
