from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def rohit (request):
    return HttpResponse ('<h1>Rohit Leads the Indian cricket Team In Worldcup Semis</h1>'
    '<h1>Rohit is one of the Best captain and also He is a Best Oepning batsman</h1>')

def virat (request):
    return HttpResponse ('<h1>Virat Completes his 50th Century in Worldcup Semis...and... He Broke Sachin records</h1>')