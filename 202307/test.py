import requests

url = 'https://jsonplaceholder.typicode.com/todos/1'

print(requests.get(url).json())


b = {1,2,3,3}
print(b)
