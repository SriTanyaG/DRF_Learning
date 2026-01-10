import requests

headers = {'Authorization':'Bearer 8182e52cfdfbf7ae2fd04865d7e44cfe054bd8e4'}
endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title":"Hello World",
    'price' : '32.99'
}
get_response = requests.post(endpoint,json=data,headers=headers)
print(get_response.json())

