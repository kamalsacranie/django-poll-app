from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

# Create your views here.

# Here we create the simplest view possible by just returning the
# HTTP response to the function called by the path function in urls
def index(request) -> HttpResponse:
    # grabbing the 5 most recent polls from our Questions model
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're looking at question {question_id}.")

def results(request, question_id: int) -> HttpResponse:
    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)

def vote(request, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're voting on question {question_id}")