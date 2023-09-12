from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.
from django.shortcuts import redirect


def add_to_cart(request, product_id):
    # Retrieve the product based on the product_id
    product = YourProductModel.objects.get(pk=product_id)

    # Check if 'cart' exists in session, if not create it as an empty dictionary
    cart = request.session.get('cart', {})

    # Check if the product is already in the cart, if not, set the quantity to 1
    cart_item = cart.get(product_id)
    if cart_item is None:
        cart[product_id] = {'quantity': 1}
    else:
        cart_item['quantity'] += 1

    # Save the updated cart to the session
    request.session['cart'] = cart

    return redirect('view_cart')  # Redirect to the cart view


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart

    return redirect('view_cart')  # Redirect to the cart view


def update_cart(request, product_id):
    new_quantity = request.POST.get('quantity')

    cart = request.session.get('cart', {})
    cart_item = cart.get(product_id)

    if cart_item:
        cart_item['quantity'] = int(new_quantity)

    request.session['cart'] = cart

    return redirect('view_cart')  # Redirect to the cart view


def view_cart(request):
    cart = request.session.get('cart', {})
    # You can retrieve product details based on the cart dictionary

    return render(request, 'cart/cart.html', {'cart': cart})


@login_required
def protected_view(request):
    # Your view logic here


SESSION_ENGINE = "django.contrib.sessions.backends.db"


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    # Your profile view logic here
