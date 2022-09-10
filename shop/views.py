from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from django.views  import View
from django.core.paginator import Paginator
from django.utils.text import slugify
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, DetailView
from .forms import ProductForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from .models import Category, Product
from profiles.models import Profile
from django.db.models import Q
from cart.cart import Cart
from contracts.models import Contract
from buyers.models import BuyerRequest
from django.http import HttpResponseRedirect
# Create your views here.

def Product_list_view(request):
    products=Product.objects.all()
    context={
        'products':products,
    }
    return render(request, 'tab_panes.html', context)

def product_list(request, category_slug=None):
    category = None
    cart = Cart(request)
    buyerrequests=BuyerRequest.objects.select_related().all()
    categories=Category.objects.all()
    products = Product.objects.select_related().filter(available=True)
    p=Paginator(products, 15)
    page=request.GET.get('page')
    products=p.get_page(page)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category,  'categories': categories, 'buyerrequests':buyerrequests, 'products': products}
    return render(request, 'home.html', context)

def product_detail(request, id):
    product = get_object_or_404(Product, id=id, available=True)
    cart_product_form = CartAddProductForm()
    total_likes=product.total_likes()
    total_dislikes=product.total_dislikes()
    context = {'product': product, 'cart_product_form': cart_product_form,'total_likes':total_likes, 'total_dislikes':total_dislikes}
    return render(request, 'shop/product/detail.html',context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    form_class=ProductForm
    template_name='shop/create_product.html'
    success_url=reverse_lazy('shop:product_list')
    def form_valid(self, form):
        form.instance.author=self.request.user
        if form.is_valid():
            prod=form.save(commit=False)
            prod.slug=slugify(prod.name)
            prod.save()
        return super().form_valid(form)


class ProductEditView(LoginRequiredMixin, UpdateView):
    
    model=Product
    template_name='shop/edit_product.html'
    success_url=reverse_lazy('shop:product_list')
    fields=['category', 'name', 'image','description','units','price', 'available' ]
    
        
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model=Product
    form_class=ProductForm
    template_name='shop/delete_product.html'
    success_url=reverse_lazy('shop:product_list')
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class MenuSearch(View):
    def get(self,  request, *args, **kwargs):
        query=self.request.GET.get('q')
        products=Product.objects.select_related().filter(
            Q(name__icontains=query)|
            Q(description__icontains=query)|
            Q(price__icontains=query)
        )
        context={
            'products':products,
        }
        return render(request, 'menusearch.html', context)

def add_like(request, pk):
    liked=False
    product=get_object_or_404(Product, pk=pk)
    product.likes.add(request.user)
    likers=product.likes.all()
    
    if request.user in likers:
        liked=True
        
    
    return HttpResponseRedirect(reverse('shop:product_detail', args=[str(product.pk)]))

def dis_like(request, pk):
    disliked=False
    product=get_object_or_404(Product, pk=pk)
    product.dislikes.add(request.user)
    dislikers=product.likes.all()
    
    if request.user in dislikers:
        disliked=True
        
    
    return HttpResponseRedirect(reverse('shop:product_detail', args=[str(product.pk)]))
        

        