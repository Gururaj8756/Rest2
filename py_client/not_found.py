import requests

endpoint="http://127.0.0.1:8000/api/products/"


get_response=requests.get(endpoint) #HTTP Request
print(get_response.json())
#print(get_response.headers)
#print(get_response.text)
print(get_response.status_code)