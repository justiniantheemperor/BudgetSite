from django.urls import path            
from .views import indexPageView, displayPageView, createBudgetPageView, editBudgetPageView, transactionInfoPageView, userInfoPageView

urlpatterns= [ 
	path("",indexPageView,name="index"),
    path('display/',displayPageView,name="display"),
    path("createbudget/", createBudgetPageView, name="createBudget"),
    path("editbudget/", editBudgetPageView, name="editBudget"),
    path("userinfo/", userInfoPageView, name="userInfo"),
    path("transactioninfo/", transactionInfoPageView, name="transactionInfo"),  
]