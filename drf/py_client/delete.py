import requests

product_id = input("Enter product id to delete: ")
try:
    product_id = int(product_id)
except:
    print("Id should be an integer")
endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete"

get_response = requests.delete(endpoint)

print(get_response.status_code,get_response.status_code==204)

