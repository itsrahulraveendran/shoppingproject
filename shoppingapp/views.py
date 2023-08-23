
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.db.models import Q
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger


# def base(request):
#     print("here 1")
#     return render(request, 'base.html')

def allproductcat(request, c_slug=None):
    print("here 2")
    global paginator_page
    c_page = None
    products_all = None

    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_all = Product.objects.all().filter(category=c_page, available=True)
    else:
        products_all = Product.objects.all().filter(available=True)

     #this for page numbering 6 is the max products in productpage
    paginator=Paginator(products_all,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    # Move the return statement outside the else block
    return render(request, "category.html", {'category': c_page, 'products': products,})
def productDetails(request,c_slug,product_slug):
    print("here 3")
    try:
        product_value=Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product_key': product_value})
