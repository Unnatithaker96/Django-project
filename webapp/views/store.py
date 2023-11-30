from django.shortcuts import render

from models.product import Product

from django.shortcuts import get_object_or_404  # to get the product and if product is not available will show 404 error
# Create your views here.

def store(request):
    
    all_products = Product.objects.all() #to reflect the products list
    
    context = {'my_products':all_products}
    
    return render(request, 'store/store.html', context)
