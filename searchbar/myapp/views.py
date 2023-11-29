from django.shortcuts import render

# Create your views here.
# views.py

from .models import Product
from .forms import ProductSearchForm

def productsearch(request):
    query = request.GET.get('query')

    if query:
        results = Product.objects.filter(name__icontains=query)
    else:
        results = []

    return render(request, 'myapp/productsearch.html', {'results': results})

