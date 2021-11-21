from django.shortcuts import render # we will use this if we want to write pages in html docs
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) : 
	return render(request, 'budgetCRUD/index.html')

def displayPageView(request) :
   return render(request, 'budgetCRUD/display.html')

def createBudgetPageView(request) :
   return render(request, 'budgetCRUD/create_budget_form.html')

def editBudgetPageView(request) :
   return render(request, 'budgetCRUD/edit_budget_form.html')

def transactionInfoPageView(request) :
   return render(request, 'budgetCRUD/transaction_info_form.html')

def userInfoPageView(request) :
   return render(request, 'budgetCRUD/user_info_form.html')