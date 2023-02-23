from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# main page
def index(request):
    return HttpResponse('Today i will go trough this tutorial and understand how create such an apps')


# Detail page
def detail(request, question_id):
    return HttpResponse('You are looking at the question of question %s' % question_id)


# Results page
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# Vote  page
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
