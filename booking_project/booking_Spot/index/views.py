from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def index(request):
    return HttpRequest("This is the place where index will be upload, index is the explanatory and initial page for the app")

