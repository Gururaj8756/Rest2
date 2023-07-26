import requests

endpoint="http://127.0.0.1:8000/api/products/{product_id}/delete/"

product_id=input("Enter ID \n")

try:
    product_id=int(product_id)

except:
    print(f'{product_id} is not Valid ')

if product_id:
    get_response=requests.delete(endpoint) #HTTP Request
    print(get_response.status_code,get_response.status_code==204)
