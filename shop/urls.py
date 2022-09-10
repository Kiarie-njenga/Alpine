from django.urls import path
from . import views







app_name = 'shop'

urlpatterns = [
    
    path('', views.product_list, name='product_list'),
    path('products/', views.Product_list_view, name='product_list_tab'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('products/menu_search/', views.MenuSearch.as_view(), name='menu_search'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
    path('products/create/', views.ProductCreateView.as_view(), name="create_product"),
    path('products/<int:pk>/edit', views.ProductEditView.as_view(), name="edit_product"),
    path('products/<int:pk>/delete', views.ProductDeleteView.as_view(), name="delete_product"),
    path('products/like/<int:pk>/', views.add_like, name='add_like'),
    path('products/dislike/<int:pk>/', views.dis_like, name='dis_like'),
]