from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, View, ListView, TemplateView
from .models import Blog, Blog_comment
from django.urls import reverse_lazy
from django.db.models import Q

from .forms import BlogForm, BlogCommentForm



class BlogCreateView(CreateView):
    form_class=BlogForm
    template_name='blogs/create.html'
    success_url=reverse_lazy('blog_list')
    
    def form_valid(self, form):
        form.instance.author=self.request.user
        
        
        return super().form_valid(form)

class BlogEditView(UpdateView):
    
    model=Blog
    template_name='blogs/edit_blog.html'
    success_url=reverse_lazy('blog_list')
    fields=['category','title','thumbnail', 'files', 'main_content',]
    
        
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class BlogDeleteView(DeleteView):
    model=Blog
    
    template_name='blogs/delete_blog.html'
    success_url=reverse_lazy('blog_list')
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class BlogSearch(View):
    def get(self,  request, *args, **kwargs):
        query=self.request.GET.get('q')
        blogs=Blog.objects.filter(
            Q(title__icontains=query)|
            Q(main_content__icontains=query)|
            Q(created_on__icontains=query)
        )
        context={
            'blogs':blogs,
        }
        return render(request, 'blogs/blog_list.html', context)

class BlogDetailView(View):
    
    def get(self,request,pk,*args,**kwargs):
        blog=Blog.objects.prefetch_related('author__profile').get(pk=pk)
        form=BlogCommentForm
        comments=Blog_comment.objects.prefetch_related('user__profile').filter(blog=blog)
        
        
        context={
            'blog':blog,
            'form':form,
            'comments':comments,
            

        }
        return render(request,'blogs/blog_detail.html', context )

     
    def post(self, request,pk,*args,**kwargs):
        blog=Blog.objects.prefetch_related('author__profile').get(pk=pk)
        form=BlogCommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.user=request.user
            new_comment.blog=blog
            new_comment.save()
        
        
        comments=Blog_comment.objects.prefetch_related('user__profile').filter(blog=blog)
        
        context={
            
            'blog':blog,
            'form':form,
            'comments':comments,
            
            
        }
        
    
        return render(request, 'blogs/blog_detail.html', context)

class BlogListView(ListView):
    model=Blog
    context_object_name='blogs'
    template_name='blogs/blog_list.html'

    
    