import requests

url = 'https://jsonplaceholder.typicode.com/todos/1'

print(requests.get(url).json())

