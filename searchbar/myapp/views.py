from django.shortcuts import render

# Create your views here.
# views.py

from .models import Product
from .forms import ProductSearchForm

def productsearch(request):
    query = request.GET.get('query')
    print("view called")
    if query:
        results = Product.objects.filter(name__icontains=query)
    else:
        results = []

    return render(request, 'productsearch.html', {'results': results})

