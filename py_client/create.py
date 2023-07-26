from email import header
import requests

endpoint="http://127.0.0.1:8000/api/products/"


headers={
    "Authorization" : 'Breaer 3064f03f8e2462961d597182a134f45fbe42a307'
}
data={
    "title":"This field is done",
    "price":32.99
}
get_response=requests.post(endpoint,json=data) #HTTP Request
print(get_response.json())
