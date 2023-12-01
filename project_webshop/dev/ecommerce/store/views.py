from django.shortcuts import render

from .models import Category , Product

from django.shortcuts import get_object_or_404  # to get the product and if product is not available will show 404 error
# Create your views here.

def store(request):
    
    all_products = Product.objects.all() #to reflect the products list
    
    context = {'my_products':all_products}
    
    return render(request, 'store/store.html', context)

# this view is created to get all the categories list

def categories(request):
    
    all_categories = Category.objects.all()
    
    return {'all_categories': all_categories}


#individual Category info from our database
def list_category(request, category_slug=None):
    
    category = get_object_or_404(Category, slug=category_slug)
    
    products = Product.objects.filter(category=category)
    
    return render(request, 'store/list-category.html', {'category':category, 'products':products} )

# individual product info from our database

def product_info(request, product_slug):
    
    product = get_object_or_404(Product, slug=product_slug)
    
    context = {'product': product}
    
    return render(request, 'store/product-info.html', context)