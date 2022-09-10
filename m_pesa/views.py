








from django.shortcuts import render
import requests
from requests.auth import HTTPBasicAuth
import json
from django.http import HttpResponse, HttpResponseRedirect
from . mpesa_credentials import  LipanaMpesaPassword
from order.models import Order
# Create your views here.


def token(request):
    consumer_key='G8M6TZuCmvQcQiBRfVlUCmO7gefcuzVm'
    consumer_secret='e5ydGFA9EwSZYCZz'
    api_url='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r=requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    access_token=r.json()
    valid_access_token=access_token['access_token']
    return valid_access_token

def lipa_na_mpesa(request, pk):
    order=Order.objects.get(pk=pk)
    total=order.get_total_cost()  
    access_token=token(request)
    api_url='https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    headers={'Authorization':'Bearer %s' % access_token}
    request={
        'BusinessShortCode':LipanaMpesaPassword.business_short_code,
        'Password':LipanaMpesaPassword.decode_password,
        'Timestamp':LipanaMpesaPassword.lipa_time,
        'TransactionType':'CustomerPayBillOnline',
        'Amount':total,
        'PartyA':254729344198,
        'PartyB':LipanaMpesaPassword.business_short_code,
        'PhoneNumber':254729344198,
        'CallBackURL':'https://sandbox.safaricom.co.ke/mpesa/',
        'AccountReference':'Alpine',
        'TranactionDesc':'Goods',
    }
    response=requests.post(api_url, json=request, headers=headers)
    return HttpResponse('success')