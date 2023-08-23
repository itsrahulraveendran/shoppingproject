from django.shortcuts import render
from shoppingapp.models import Product
#for more things using Q
from django.db.models import Q
# Create your views here.
def SearchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=query) | Q(productdiscr__contains=query))
    return render(request,'search.html',{'query_key':query, 'products_key':products})

