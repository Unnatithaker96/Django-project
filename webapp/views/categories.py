from django.shortcuts import render
from django.shortcuts import get_object_or_404  # to get the product and if product is not available will show 404 error

from webapp.models.category import Category
from webapp.models.product import Product

def categories(request):
    
    all_categories = Category.objects.all()
    
    return {'all_categories': all_categories}

def list_category(request, category_slug=None):
    
    category = get_object_or_404(Category, slug=category_slug)
    
    products = Product.objects.filter(category=category)
    
    return render(request, 'store/list-category.html', {'category':category, 'products':products} )
