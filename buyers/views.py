








from django.shortcuts import render
from .models import BuyerRequest, Comment
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  View, CreateView, UpdateView, DeleteView, ListView
from .forms import BuyerRequestForm, CommentForm

# Create your views here.


class BuyersRequestCreateView(LoginRequiredMixin, CreateView):
    form_class=BuyerRequestForm
    success_url=reverse_lazy('shop:product_list')
    template_name="buyers/create.html"

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class BuyersRequestUpdateView(LoginRequiredMixin,UpdateView): # new
    model = BuyerRequest
    fields = ('title', 'body','pic',)
    template_name = 'buyers/request_edit.html'
    success_url = reverse_lazy('shop:product_list')
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class BuyerRequestDeleteView(LoginRequiredMixin,DeleteView):
     model = BuyerRequest
     template_name = 'buyers/request_delete.html'
     success_url = reverse_lazy('shop:product_list')

     def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)




class BuyerRequestDetail(View):
    
    def get(self,request,pk,*args,**kwargs):
        buyerrequest=BuyerRequest.objects.prefetch_related('user__profile').get(pk=pk)
        form=CommentForm
        comments=Comment.objects.prefetch_related('author__profile').filter(buyer_request=buyerrequest)
        
        
        context={
            'buyerrequest':buyerrequest,
            'form':form,
            'comments':comments,
            

        }
        return render(request,'buyers/buyer_request_detail.html', context )

     
    def post(self, request,pk,*args,**kwargs):
        buyerrequest=BuyerRequest.objects.prefetch_related('user__profile').get(pk=pk)
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.author=request.user
            new_comment.buyer_request=buyerrequest
            new_comment.save()
        
        
        comments=Comment.objects.prefetch_related('author__profile').filter(buyer_request=buyerrequest)
        
        context={
            
            'buyerrequest':buyerrequest,
            'form':form,
            'comments':comments,
            
            
        }
        
    
        return render(request, 'buyers/buyer_request_detail.html', context)

class CommentDeleteView(DeleteView):
    model=Comment
    template_name='buyers/comment_delete.html'
    def get_success_url(self):
        pk=self.kwargs['post_pk']
        return reverse_lazy('buyer_request__detail', kwargs={'pk':pk})


    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class BuyerRequestListView(ListView):
    model=BuyerRequest
    template_name='home.html'
    context_object_name='buyerrequests'