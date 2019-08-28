from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Q

def index(request):
    categories = Category.objects.all()
    return render(request,'shop/product/index.html',{'categories':categories})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    query=request.GET.get("q")
    if query:
        products=products.filter(Q(name__icontains=query)).distinct()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    paginator=Paginator(products,6 )
    page_number=request.GET.get('page')
    try:
        posts=paginator.page(page_number)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    return render(request,'shop/product/list.html',{'category': category,'categories': categories,'products': products,'posts':posts})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id,slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    return render(request,'shop/product/detail.html',{'product': product,'cart_product_form': cart_product_form})
