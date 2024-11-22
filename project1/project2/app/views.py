from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def sarkar(request):
    return HttpResponse('test file 1')

def good(request):
    return HttpResponse('<h1>firsterror<h1/>')
