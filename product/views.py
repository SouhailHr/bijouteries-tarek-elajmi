from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product

# Create your views here.

def all_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, "allproducts.html", {"products": products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "productdetail.html", {"product": product})

def product_filter(request, category):
    products = Product.objects.filter(category=category)
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, "products.html", {"products": products})