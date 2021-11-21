from django.urls import path
from . import views

app_name="buyer"
urlpatterns = [
	path('home/', views.home),
	path('cart/<int:id>/', views.cart, name="addcart"),
	path('cartdetails/', views.cartdetails),
	path('cartcalculate/', views.cartcal),
	path('delcart/<int:id>/', views.delcart, name="delcart"),
	path('ALLDelete/<int:id>/', views.AllDelete, name="AllDelete")
]	