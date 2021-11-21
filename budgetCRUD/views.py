from django.shortcuts import render # we will use this if we want to write pages in html docs
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) : 
	return render(request, 'budgetCRUD/index.html')

def displayPageView(request) :
   return render(request, 'budgetCRUD/display.html')