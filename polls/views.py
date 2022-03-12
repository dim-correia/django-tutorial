from django.http import HttpResponse

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_test for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse(f"Question {question_id}")

def results(request, question_id):
    return HttpResponse(f"Results of {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Vote for {question_id}")

