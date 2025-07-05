from rest_framework.response import Response
import requests

# Credential
def credentials():
    data = {
        "username": "faiyas",
        "password": "faiyas"
    }
    return data

# Refresh Token API
def acessToken():
    toke_url = 'http://127.0.0.1:8000/api/token/'
    data = {
        "username": "faiyas",
        "password": "faiyas"
    }

    return (requests.post(toke_url, json=data))
