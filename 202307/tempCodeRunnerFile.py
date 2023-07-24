import requests
from pprint import pprint as print

dummy_data = []

API_URL = 'https://jsonplaceholder.typicode.com/users/'
response = requests.get(API_URL)
parsed_data = response.json()

for i in range(10):
    user_data = parsed_data[i]
    user_info = {"name" : user_data['name'], "lat" : user_data['address']['geo']['lat'], "lng" : user_data['address']['geo']['lng'], "companyname" : user_data['company']['name']}
    if float(user_info['lat']) >= 80 or float(user_info['lat']) <= -80:
        continue
    if float(user_info['lng']) >= 80 or float(user_info['lng']) <= -80:
        continue
    dummy_data.append(user_info)

print(dummy_data)
