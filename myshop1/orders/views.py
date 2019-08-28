from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.shortcuts import render, redirect
from django.urls import reverse
from .tasks import order_created
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Order
#from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from .tasks import order_created

#@login_required
def order_create(request):
    cart = Cart(request)
    order=''
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
            cart.clear()
            order_created.delay(order.id) # set the order in the session
            request.session['order_id'] = order.id # redirect to the payment
            return redirect(reverse('payment:process'))

    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})

@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,'admin/orders/order/detail.html',{'order': order})

def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            user=form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request,f' Account Created Successfully for {username} ! Now you can Login')
            return HttpResponseRedirect('/accounts/login')
    return render(request,'orders/signup.html',{'form':form})

def logout_view(request):
    return render(request,'orders/logout.html')
