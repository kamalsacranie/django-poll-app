from django.http import (
    HttpResponse, 
    Http404, 
    HttpResponseRedirect,
)

from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Choice

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

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id: int) -> HttpResponse:
    # Getting the relevant object using the get or 404 shortcut
    question = get_object_or_404(Question, pk=question_id)

    # Using the POST data from form and trying to assign it to the choice
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # rendering the form again
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))