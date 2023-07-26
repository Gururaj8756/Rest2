import requests

endpoint="http://127.0.0.1:8000/api/products/1/update/"

data={
    'title':"Hello world my old",
    'price':299.99
}


get_response=requests.put(endpoint,json=data) #HTTP Request
print(get_response.json())
#print(get_response.headers)
#print(get_response.text)
print(get_response.status_code)