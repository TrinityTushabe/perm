from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Product, CartItem, Category
from .forms import CartItemForm


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with your home page URL
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = CartItemForm()

    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart_item, created = CartItem.objects.get_or_create(
                user=request.user,
                product=product,
                defaults={'quantity': quantity}
            )
            if not created:
                cart_item.quantity += quantity
                cart_item.save()

    context = {'product': product, 'form': form}
    return render(request, 'product_detail.html', context)

def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    context = {'cart_items': cart_items}
    return render(request, 'cart.html', context)

def checkout_view(request):
    # Perform checkout logic (e.g., create an order, handle payments, etc.)
    # For simplicity, we'll just clear the user's cart in this example.
    CartItem.objects.filter(user=request.user).delete()
    return render(request, 'checkout.html')

def home_view(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'home.html',{'products':products})


def index_view(request):
    return render(request, 'index.html')

def product_list(request, category_name=None):
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_name:
        category = Category.objects.get(name=category_name)
        products = products.filter(category=category)

    context = {'categories': categories, 'products': products}
    return render(request, 'product_list.html', context)


def product_list_category(request, category_name):
    category = Category.objects.get(name=category_name)
    products = Product.objects.filter(category=category)
    context = {'category': category, 'products': products}
    return render(request, 'product_list_category.html', context)
