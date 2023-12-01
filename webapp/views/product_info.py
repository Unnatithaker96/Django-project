from django.shortcuts import render

from webapp.models.product import Product
from django.shortcuts import get_object_or_404  # to get the product and if product is not available will show 404 error

def product_info(request, product_slug):
    
    product = get_object_or_404(Product, slug=product_slug)
    
    context = {'product': product}
    
    return render(request, 'store/product-info.html', context)
