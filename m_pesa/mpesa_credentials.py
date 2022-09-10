










import requests
import json
import base64
from datetime import datetime
from requests.auth import HTTPBasicAuth

#class MpesaC2BCredential:
    #consumer_key='G8M6TZuCmvQcQiBRfVlUCmO7gefcuzVm'
    #consumer_secret='e5ydGFA9EwSZYCZz'
    #api_url='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

#class MpesaAccessToken:
    #r=requests.get(MpesaC2BCredential.api_url, auth=HTTPBasicAuth(MpesaC2BCredential.consumer_key, MpesaC2BCredential.consumer_secret))
    #access_token=r.json()
    #valid_access_token=access_token['access_token']

class LipanaMpesaPassword:
    lipa_time=datetime.now().strftime('%Y%m%d%H%M%S')
    business_short_code='174379'
    passkey='bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    data_to_encode=business_short_code + passkey + lipa_time
    online_password=base64.b64encode(data_to_encode.encode())
    decode_password=online_password.decode('utf-8')
