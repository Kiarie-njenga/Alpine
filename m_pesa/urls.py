







from django.urls import path
from . import views

urlpatterns=[
    path('access-token/', views.token, name='token'),
    path('online/lipa/<int:pk>', views.lipa_na_mpesa, name='lipa_na_mpesa'),
]