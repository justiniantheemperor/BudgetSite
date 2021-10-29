from django.urls import path            
from .views import indexPageView, displayPageView

urlpatterns= [ 
	path("",indexPageView,name="index"),
    path('display',displayPageView,name="display")
]