from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world from polls")

def detail(request, question_id):
    return HttpResponse(f"Question {question_id}")

def results(request, question_id):
    return HttpResponse(f"Results of {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Vote for {question_id}")