





from django.views import View
from django.shortcuts import render, get_object_or_404
from shop.models import Product
from .models import Profile
from datetime import timedelta
from django.utils.timezone import datetime
from order.models import Order, OrderItem
from django.views.generic import UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from blogs.models import Blog
from contracts.models import Contract
# Create your views here.

class ProfileView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        profile=Profile.objects.get(pk=pk)
        user=profile.user
        vis=request.user.pk
        products=Product.objects.filter(author=user).order_by('created')
        order_item=OrderItem.objects.filter(product__author__id=user.id)
        blogs=Blog.objects.filter(author=user)
        contracts=Contract.objects.filter(author=user)
        orders=Order.objects.filter(items__id__in=order_item)
        order_items=OrderItem.objects.filter(product__author=request.user,  order__id__in=orders)
        total_rev=0
        for order_price in order_items:
            total_rev+=order_price.price

        owner=False
        if request.user==user:
            owner=True
        context={
            'user':user,
            'profile':profile,
            'products':products,
            'blogs':blogs,
            'contracts':contracts,
            'orders':orders,
            'total_rev':total_rev,
            'total_orders':len(orders),
            'owner':owner,
            'vis':vis,
        }
        return render(request, 'profile/profile.html', context)


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model=Profile  
    template_name='profile/profile_edit.html' 
    fields=['name', 'bio', 'date_of_birth','phone' ,'location','what_describes_you' ,'pic'] 
    
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

#class ProfileOrderDetail(DetailView):
    #model=Order
    #template_name= 'profile/profile_order_detail.html'
    
    #context_object_name='order'
@login_required
def get_ordered_items(request, pk):
    order=get_object_or_404(Order, pk=pk)
    order_items=OrderItem.objects.filter(product__author=request.user,  order=order)
    
    context={
        'order':order,
        'order_items':order_items,
        
    }
    return render(request, 'profile/profile_order_detail.html', context)

def get_sent_items(request):
    orders=Order.objects.filter(user=request.user)
    context={
        'orders':orders,
    }
    return render(request, 'profile/sent_orders.html', context)


    
    


    

    

    
        

