from django.db import models
from django.urls import reverse
class Product(models.Model):

    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    productdiscr=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    # category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product', blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    def get_url(self):
     return reverse('shoppingapp:PoductCat_urls', args=[self.category.slug,self.slug])

from django.db import models

# Create your models here.
