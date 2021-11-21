from django.shortcuts import render, redirect
from seller.models import Products
from django.contrib.auth.models import User
from .models import Cart
from django.contrib import messages

# Create your views here.
def home(request):
	pobjs = Products.objects.all()

	uobj = User.objects.get(username=request.user)
	cnt = Cart.objects.filter(user_id=uobj.id).count()
	return render(request, "WelcomeBuyer.html", {'objs' : pobjs, 'cnt': cnt})


def cart(request, id):
	pobj = Products.objects.get(id=id)
	uobj = User.objects.get(username=request.user)

	try:

		c = Cart(user=uobj, product=pobj)
		c.save()
		messages.success(request, "Added Successfully")
		return redirect('/buyer/home/')
	except:
		messages.error(request, "Already Added")
		return redirect("/buyer/home/")

def cartdetails(request):
	uobj = User.objects.get(username=request.user)
	cartobjs = Cart.objects.filter(user_id=uobj.id)

	items = []
	for i in cartobjs:
		items.append(Products.objects.get(id=i.product_id))
	return render(request, "CartDetails.html", {'pobjs': items})	

def cartcal(request):
	pqtys = request.POST.getlist('pqty')	#[2,3]
	prices = request.POST.getlist('price') #[200, 300]
	pids = request.POST.getlist('pid') #[1,3]

	amt = 0
	for i in range(len(pqtys)):
		amt = amt + (float(prices[i])*int(pqtys[i]))

		pobj = Products.objects.filter(id=pids[i])
		updatedqty = pobj[0].qty - int(pqtys[i])
		pobj.update(qty=updatedqty)

		#Total amount
		#Update stock
		# cart clear
		# order creation
	return render(request, "OrderUpdate.html", {'amt':amt})


def delcart(request, id):
    cart = Cart(request.session)
    Product = Products.objects.get(id=id)
    Cart.delete(Product)
 
    return redirect("/buyer/cartdetails/")

def AllDelete(request, id):
		cart=Cart.objects.get(id=id)
		cart.Products.objects.all().delete()
		cart.amt=0
		cart.save()
		return redirect(request,'/cartdetails/')
	   
	


















