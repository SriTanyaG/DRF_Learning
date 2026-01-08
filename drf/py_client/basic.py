import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"
get_response = requests.post(endpoint,json = {"title":"Hello World"}, params = {"abc":123}) # HTTP request
# print(get_response.headers)
# print(get_response.text) #Print raw text response

# 1.HTTP request will give HTML response
# 2.A REST API HTTP Request will give JSON response

# JavaScript Object Notation ~ A python Dict

print(get_response.json())

# {'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.5', 'X-Amzn-Trace-Id': 'Root=1-695e059e-2476e9b33e1ac8fe1fc1d7e2'}, 'json': None, 'method': 'GET', 'origin': '103.16.202.221', 'url': 'https://httpbin.org/anything'}

# print(get_response.status_code)