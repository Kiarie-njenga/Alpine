







from django.urls import path
from . import views

urlpatterns=[
    path('list', views.BlogListView.as_view(), name='blog_list'),
    path('search', views.BlogSearch.as_view(), name='blog_search'),
    path('blogs/create/', views.BlogCreateView.as_view(), name="create_blog"),
    path('blogs/<int:pk>/edit', views.BlogEditView.as_view(), name="edit_blog"),
    path('blogs/<int:pk>/delete', views.BlogDeleteView.as_view(), name="delete_blog"),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
]