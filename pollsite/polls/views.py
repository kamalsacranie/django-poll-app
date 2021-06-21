from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .models import Question

# Create your views here.

# Here we create the simplest view possible by just returning the
# HTTP response to the function called by the path function in urls
def index(request) -> HttpResponse:

    # grabbing the 5 most recent polls from our Questions model
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    
    return render(request, 'polls/index.html', context=context)

def detail(request, question_id: int) -> HttpResponse:
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render (request, 'polls/detail.html', {'question': question})

def results(request, question_id: int) -> HttpResponse:
    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)

def vote(request, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're voting on question {question_id}")