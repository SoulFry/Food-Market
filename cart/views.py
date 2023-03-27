from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from cafes.models import CafeMenu
from .cart import Cart
from .forms import CartAddProduct


# Create your views here.
def cart_add(request, object_id):
    if request.method == 'POST':
        cart = Cart(request)
        product = get_object_or_404(CafeMenu, id=object_id)
        form = CartAddProduct(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(object=product,
                     count=cd['count'],
                     update_count=cd['update'])
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, object_id):
    cart = Cart(request)
    product = get_object_or_404(CafeMenu, id=object_id)
    cart.remove(product)
    return redirect('cart:cart-detail')


def cart_detail(request):
    cart = Cart(request)
    if cart.session._session['cart'] == {}:
        return render(request, 'cart-empty.html')
    else:
        return render(request, 'cart-detail.html', {'cart': cart})

