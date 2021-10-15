from django.shortcuts import render
from django.http import HttpResponse
from .models

def index(request):
    products = Product.objects.all()
    print(products)
    params = {}
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