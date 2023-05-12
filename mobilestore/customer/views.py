from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView,FormView,CreateView,UpdateView
from store.models import *
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Cart, CartItem, MyOrders, OrderItems
from .forms import AddToCartForm
from django.db.models import Q

# Create your views here.

class Chome(TemplateView):
    template_name="custhome.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = Mobile.objects.all().order_by('-datetime')
        context["reviews"] = OrderItems.objects.all()
        return context
    
class Cpro(TemplateView):
    template_name="custprofile.html"
    
    

    
class Myorder(TemplateView):
    template_name="myorder.html"
    

def view_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        total_price = sum([item.product.price * item.quantity for item in cart_items])
    except Cart.DoesNotExist:
        cart = None
        cart_items = None
        total_price = 0

    context = {'cart': cart, 'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'cart.html', context)


def remove_item(request,item_id):
    product=get_object_or_404(CartItem,pk=item_id)   
    product.delete()
    return redirect('cart')



# def add_to_cart(request, product_id):
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     product = Mobile.objects.get(pk=product_id)

   

def cart(request):
    cart = request.user.cart
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum([item.product.price * item.quantity for item in cart_items])
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart.html', context)

def add_to_cart(request, product_id):
    product = get_object_or_404(Mobile, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            cart_item.quantity = quantity
            cart_item.save()
            return redirect('cart')
    else:
        form = AddToCartForm()
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'add_to_cart.html', context)

def checkout(request):
    cart_items = CartItem.objects.filter(cart__user=request.user).all()
    total = 0
    for item in cart_items:
        total += item.quantity * item.product.price
    context = {
        'cart_items': cart_items,
        "sub_total": total,
    }
    return render(request, "checkout.html", context)


def complete_checkout(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    total = 0
    address = request.POST.get("address")
    print(address)
    for item in cart_items:
        total += item.quantity * item.product.price
        
    new_order = MyOrders.objects.create(user=request.user, sub_total=total, address=address)
    
    for item in cart_items:
        OrderItems.objects.create(order=new_order, product=item.product, quantity=item.quantity)
        
    cart_items.delete() 
    return redirect(myorders)


def myorders(request):
    orders = MyOrders.objects.filter(user=request.user).all()
    order_items = OrderItems.objects.filter(order__user=request.user).all()
    context = {
        "orders": orders,
        "order_items": order_items,
    }
    return render(request, "myorder.html", context)


def submit_review(request):
    text = request.POST.get('text', '')
    id = request.POST.get('id', '')
    OrderItems.objects.filter(id=id).update(review=text)
    return redirect(myorders)
        

def search(request):
    key = request.GET.get('key', '')
    products = Mobile.objects.filter(Q(brand__icontains=key) | Q(model__icontains=key)).all() 
    context = {
        'data': products,
    }
    return render(request, "search.html", context)