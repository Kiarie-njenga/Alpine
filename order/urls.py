from django.urls import path
from . import views







app_name = 'order'

urlpatterns = [
    path('order/', views.order_create, name='order_create'),
    path('order/<int:pk>', views.OrderConfirmation.as_view(), name='order_confirmation'),
    path('payment_confirmation/', views.OrderPayConfirmation.as_view(), name='payment_confirmation'),
    path('order/<int:pk>/edit', views.OrderEditView.as_view(), name="order_edit"),
    

]