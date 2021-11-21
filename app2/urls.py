from django.urls import path
from .views import  PurchegerApiView

urlpatterns = [
	path('Purchegerdata/', PurchegerApiView.as_view()),

]