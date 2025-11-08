from django.shortcuts import render
from django.http import HttpResponse

def show_error(request):
    1/0
    return HttpResponse("Execution will not reach here")