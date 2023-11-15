from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def kane (request):
    return HttpResponse ('<h1><center>kane Williamson is the Most unluckiest Captain In World Cricket</center></h1>')

def conway (request):
    return HttpResponse ('<h1><marquee>Conway is the Left-Hand Opening Batter in New zeland</marquee></h1>')