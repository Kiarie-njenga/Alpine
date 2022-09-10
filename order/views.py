from django.shortcuts import render, redirect
from cart.cart import Cart
from .models import OrderItem
import json
from .models import Order




from django.urls import reverse_lazy

from django.views.generic import UpdateView
from django.core.mail import send_mail
from django.http import JsonResponse
from .forms import OrderCreateForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
def order_create(request):
    cart = Cart(request)
    n=cart.get_total_price_after_discount()
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        
        if form.is_valid():

            order = form.save(commit=False)
            order.user=request.user
            order.save()
            
            for item in cart:

                OrderItem.objects.create(order=order, product=item['product'],
                                         price=float(n), quantity=item['quantity'])
            # clear the cart
        #send email to the user after eeverything is done
            body=('Thank you for your order! Your stock is being processed and will be delivered soon upon payment')
            send_mail(
                 'Thank you for your order',
                 body,
                 'Alpine.com',
                 [order.email],
                 fail_silently=False
            )
        

            
            return redirect('order:order_confirmation', pk=order.pk)
            
    else:
        form = OrderCreateForm()
    return render(request, 'order/create.html', {'cart': cart, 'form': form}) 

class OrderConfirmation(View):
    
    def get(self, request, pk, *args, **kwargs):
        order = Order.objects.get(pk=pk)
        cart=OrderItem.objects.filter(order=order)
        total=order.get_total_cost

        
            
        context = {
            'order':order,
            'cart':cart,
            'total':total,
        }

        return render(request, 'order/created.html', context)
    
    def post(self, request, pk, *args, **kwargs):
        cart = Cart(request)
        data = json.loads(request.body)

        if data['paid']:
            order = Order.objects.get(pk=pk)
            order.paid = True
            order.save()
            cart.clear()

            return redirect('order:payment_confirmation')
        else:
            order = Order.objects.get(pk=pk)
            cart=OrderItem.objects.filter(order=order)
            total=order.get_total_cost  
            
        
            
            context = {
                'order':order,
                'cart':cart,
                'total':total,
            }
            return render(request, 'order/created.html', context)


class OrderPayConfirmation(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        cart.clear()
        return render(request, 'order/checkout.html')

class OrderEditView(LoginRequiredMixin, UpdateView):
    model=Order  
    template_name='order/order_edit.html' 
    fields=['first_name', 'last_name', 'address', 'is_delivered'] 
    success_url=reverse_lazy('profiles:sent_orders')
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)