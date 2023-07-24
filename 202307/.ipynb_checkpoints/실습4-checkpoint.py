# 실습 4-1
import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/1'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()

# 응답 데이터 출력
print(response)

# 변환 데이터 출력
print(parsed_data)
# 변환 데이터의 타입
print(type(parsed_data))

# 특정 데이터 출력
print(parsed_data['name'])
print(parsed_data['username'])
print(parsed_data['company']['name'])


# 실습 4-2
import requests
from pprint import pprint as print

dummy_data = []

for i in range(1,11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/' + str(i)
    response = requests.get(API_URL)
    parsed_data = response.json()
    dummy_data.append(parsed_data['name'])

print(dummy_data)


import requests
from pprint import pprint as print

dummy_data = []

API_URL = 'https://jsonplaceholder.typicode.com/users/'
response = requests.get(API_URL)
parsed_data = response.json()
dummy_data.append(parsed_data['name'])

print(dummy_data)


# 실습 4-3

import requests
from pprint import pprint as print

dummy_data = []

API_URL = 'https://jsonplaceholder.typicode.com/users/'
response = requests.get(API_URL)
parsed_data = response.json()

for i in range(10):
    user_data = parsed_data[i]
    user_info = {"name" : user_data['name'], "lat" : user_data['address']['geo']['lat'], "lng" : user_data['address']['geo']['lng'], "companyname" : user_data['company']['name']}
    if user_info['lat']
    dummy_data.append(user_info)
