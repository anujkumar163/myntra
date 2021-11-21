from django.shortcuts import render, redirect
from .models import Category, Products
from django.contrib.auth.models import User

# Create your views here.
def home(request):
	return render(request, "WelcomeSeller.html")

def add_product(request):
	cobj = Category.objects.all()
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

	return render(request, "add_product.html", {'catobjs' : cobj})