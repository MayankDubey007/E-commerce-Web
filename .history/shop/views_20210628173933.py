from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil  

def index(request):
    products = Product.objects.all()
    # print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    # params = {'no_of_slide':nSlides,'range':range(1,nSlides),'product':products}
    allprods = [[products, range()],[],[],[]]
    return render(request,'shop/index.html',params)











def about(request):
    return HttpResponse("ABOUT")
def contact(request):
    return HttpResponse("CONTACT")
def tracker(request):
    return HttpResponse("TRACKER")
def search(request):
    return HttpResponse("SEARCH")
def productview(request):
    return HttpResponse("PRODUCT VIEW")
def checkout(request):
    return HttpResponse("CHECKOUT")