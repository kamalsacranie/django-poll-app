from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Here we create the simplest view possible by just returning the
# HTTP response to the function called by the path function in urls
def index(request) -> HttpResponse:
    return HttpResponse("Hello, world")

def detail(request, question_id) -> HttpResponse:
    return HttpResponse(f"You're looking at question {question_id}.")

def results(request, question_id) -> HttpResponse:
    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)

def vote(request, question_id) -> HttpResponse:
    return HttpResponse(f"You're voting on question {question_id}")