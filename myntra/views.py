from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
	return render(request, "index.html")


def webpage0(request):
	return render(request, "login_pageSecond.html")

def webpage1(request):
	return render(request, "Signup_page.html")	

def webpage2(request):
	return render(request, "product_detail.html")

def cartdetails(request):
	return render(request, "CartDetails.html")
	'''uobj = User.objects.get(username=request.user)
	cartobjs = Cart.objects.filter(user_id=uobj.id)

	items = []
	for i in cartobjs:
		items.append(Products.objects.get(id=i.product_id))
	return render(request, "CartDetails.html", {'pobjs': items})'''	


def add_product(request):
	return render(request, "add_product.html")

	'''cobj = Category.objects.all()
	if request.method == "POST":
		title = request.POST['title']
		desc = request.POST['desc']
		pr = request.POST['price']
		qty = request.POST['qty']
		pimg = request.FILES['pimg']
		catid = request.POST['cid']

		cobj = Category.objects.get(id=catid)
		uobj = User.objects.get(username=request.user)

		p = Products(title=title, desc=desc, price=pr, qty=qty, pro_img=pimg, category=cobj, added_by=uobj)
		p.save()
		return redirect('/seller/add_product/')

	return render(request, "add_product.html", {'catobjs' : cobj})'''

def signup(request):
	if request.method == "POST":
		nm = request.POST['nm']
		uname = request.POST['un']
		pwd = request.POST['pwd']
		role = request.POST['role']
		su = 0
		staff = 0

		if role == "seller":
			su = 1
		elif role == "buyer":
			staff = 1

		u = User(first_name=nm, username=uname, password=make_password(pwd), is_superuser=su, is_staff=staff)
		u.save()
		return redirect('/signup/')
	return render(request, "Signup_page.html")


def login_call(request):
	if request.method == "POST":
		uname = request.POST['un']
		pwd = request.POST['pwd']

		user = authenticate(username=uname, password=pwd)
		print(user)

		if user:
			login(request, user)
			if user.is_superuser:
				
				return redirect('/seller/home/')
			elif user.is_staff:
				
				return redirect('/buyer/home/')
			
		else:

			return redirect('/login/')
		
	return render(request, "login_pageSecond.html")

def logout_call(request):
	logout(request)
	return redirect('/login/')