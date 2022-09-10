from django.shortcuts import render

# Create your views here.






from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, View, ListView, TemplateView
from .models import Contract, Con_comment
from django.urls import reverse_lazy
from django.db.models import Q
from profiles.models import Profile
from .forms import ContractForm, CommentForm

class ContractCreateView(CreateView):
    form_class=ContractForm
    template_name='contracts/create.html'
    success_url=reverse_lazy('contract:contract_list')
    
    def form_valid(self, form):
        form.instance.author=self.request.user
        
        
        return super().form_valid(form)

class ContractEditView(UpdateView):
    
    model=Contract
    template_name='contracts/edit_contract.html'
    success_url=reverse_lazy('contract:contract_list')
    fields=['title', 'start_of_contract', 'end_of_contract','is_active','payment_cost_details', 'project_specific_details' , 'legal_disclaimers']
    
        
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ContractDeleteView(DeleteView):
    model=Contract
    
    template_name='contracts/delete_contract.html'
    success_url=reverse_lazy('contract:contract_list')
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ContractSearch(View):
    def get(self,  request, *args, **kwargs):
        query=self.request.GET.get('q')
        contracts=Contract.objects.filter(
            Q(title__icontains=query)|
            Q(payment_cost_details__icontains=query)|
            Q(project_specific_details__icontains=query)
        )
        context={
            'contracts':contracts,
        }
        return render(request, 'contracts/contract_list.html', context)

class ContractDetailView(View):
    
    def get(self,request,pk,*args,**kwargs):
        contract=Contract.objects.prefetch_related('author__profile').get(pk=pk)
        form=CommentForm
        comments=Con_comment.objects.prefetch_related('user__profile').filter(contract=contract)
        
        
        context={
            'contract':contract,
            'form':form,
            'comments':comments,
            
            

        }
        return render(request,'contracts/contract_detail.html', context )

     
    def post(self, request,pk,*args,**kwargs):
        contract=Contract.objects.prefetch_related('author__profile').get(pk=pk)
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.user=request.user
            new_comment.contract=contract
            new_comment.save()
        
        
        comments=Con_comment.objects.prefetch_related('user__profile').filter(contract=contract)
        
        context={
            
            'contract':contract,
            'form':form,
            'comments':comments,
            
            
        }
        
    
        return render(request, 'contracts/contract_detail.html', context)

class CommentDeleteView(DeleteView):
    model=Con_comment
    template_name='contracts/comment_delete.html'
    def get_success_url(self):
        pk=self.kwargs['contract_pk']
        return reverse_lazy('contract__detail', kwargs={'pk':pk})


    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ContractListView(ListView):
    model=Contract
    context_object_name='contracts'
    template_name='contracts/contract_list.html'


