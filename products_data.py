import requests

# data  = requests.get('http://127.0.0.1:8000/api/products/',auth=('cognoai','1234'))
# print(data.json())

product_image = open('/Users/rajkumarjuvva/Downloads/black_grapes.jpg','rb')
body = {"name":"Black Grapes",'cost':37,'description':'These grapes are from heaven'}
# response = requests.post('http://127.0.0.1:8000/api/products/',auth=('cognoai','1234'),data=body,files = {'file':product_image})
# print(response)
requests.get()

data = {"product_id":1,"quantity":10}
response = requests.post('http://127.0.0.1:8000/api/add_to_cart/',auth=('cognoai','1234'),data=data)
print(response.json())