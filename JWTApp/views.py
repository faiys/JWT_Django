# Library
from django.http import HttpResponse
import requests

# Rest API
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status

#Call modules
from . import utils

class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            content = {'code': status.HTTP_200_OK ,'message': 'success','json':[{'name':'Mohamed', "id":100},{'name':'Faiyas', "id":101},{'name':'Ali', "id":102}]}
        except:
            content = {'code': status.HTTP_200_OK ,'message': 'success','json':[]}
        return Response(content, status=status.HTTP_200_OK)

# Get API
def getapi(self):
    token_API = utils.acessToken().json()
    headers = {
        'Authorization': f'Bearer '+token_API['access']
    }
    credential = utils.credentials()
    get_resp = requests.get("http://127.0.0.1:8000/",json=credential, headers=headers)
    json_resp = get_resp.json()
    if(json_resp['code'] == 200  and json_resp['message'] == 'success'):
        main_json = json_resp['json']
        return HttpResponse(main_json)
    else:
        return HttpResponse(get_resp)

    
    