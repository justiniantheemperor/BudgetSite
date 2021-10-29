from django.shortcuts import render # we will use this if we want to write pages in html docs
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) : 
	return HttpResponse('This is the main page')

def displayPageView(request) :
    return HttpResponse('This is the display page')