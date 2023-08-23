from . import views
from django.urls import path
app_name='shoppingapp'
urlpatterns = [
    # path('',views.base,name='base'),
    path('',views.allproductcat,name='allproductcat'),
    path('<slug:c_slug>/',views.allproductcat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.productDetails,name='PoductCat_urls')
]
