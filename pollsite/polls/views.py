from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Here we create the simplest view possible by just returning the
# HTTP response to the function called by the path function in urls
def index(request) -> HttpResponse:
    return HttpResponse("Hello, world")