from django.views import View
from .models import Product, Category, Order, CustomUser
from .forms import RegisterForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.hashers import check_password

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart', {}).keys())
        products = Product.get_products_by_id(ids)
        return render(request, 'cart.html', {'products': products})


def categories(request):
    all_categories = Category.objects.all()
    return render(request, 'categories.html', {'all_categories': all_categories})

def list_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/list-category.html', {'category': category, 'products': products})


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        user = request.session.get('customuser')
        cart = request.session.get('cart', {})
        products = Product.get_products_by_id(list(cart.keys()))
        for product in products:
            order = Order(user=CustomUser(id=user),
                          product=product,
                          price=product.price,
                          address=address,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}
        return redirect('cart')

class OrderView(View):
    def get(self, request):
        user = request.session.get('user')
        orders = Order.get_orders_by_user(user)
        return render(request, 'orders.html', {'orders': orders})


def product_info(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    context = {'product': product}
    return render(request, 'store/product-info.html', context)

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

def store(request):
    all_products = Product.objects.all()
    context = {'my_products': all_products}
    return render(request, 'store/store.html', context)

class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'login.html')

    def post(self, request):
        email = request.POST.get ('email')
        password = request.POST.get ('password')
        customer = CustomUser.get_customer_by_email (email)
        error_message = None
        if customer:
            flag = check_password (password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect (Login.return_url)
                else:
                    Login.return_url = None
                    return redirect ('homepage')
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid !!'

        print (email, password)
        return render (request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')
