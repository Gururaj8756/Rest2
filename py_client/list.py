from email import header
import requests
from getpass import getpass
auth_endpoint="http://localhost:8000/api/auth/"
username=input("What is your username ")
password=getpass("Enter pass ")

auth_response=requests.post(auth_endpoint,json={"username":"Guru","password":password})
print(auth_response.json())

if auth_response.status_code ==200:
    token=auth_response.json()['token']
    headers={
        "Authorization": f'Breaer {token} '
    }

    endpoint="http://localhost:8000/api/products/"
    get_response=requests.get(endpoint,headers=headers) #HTTP Request
    print(get_response.json())
