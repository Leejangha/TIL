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

API_URL = 'https://jsonplaceholder.typicode.com/users/'
response = requests.get(API_URL)
parsed_data = response.json()

parsed_data_slice = []

for i in range(10):
    parsed_data_slice.append(parsed_data[i])
    dummy_data.append(parsed_data_slice[i]['name'])

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
    if float(user_info['lat']) >= 80 or float(user_info['lat']) <= -80:
        continue
    if float(user_info['lng']) >= 80 or float(user_info['lng']) <= -80:
        continue
    dummy_data.append(user_info)

print(dummy_data)


# 실습 4-4

black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

import requests

dummy_data = []
censored_user_list = {}

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

def create_user():
    for i in range(len(dummy_data)):
        user_data = dummy_data[i]
        user_info = {user_data['companyname'] : user_data['name']}
        if censorship(user_info) == True:
            for company, name in user_info.items():
                censored_user_list.setdefault(company, [name])
    print(censored_user_list)

    return
    
def censorship(x):
    for company, name in x.items():
        if company in black_list:
            print(f'{company} 소속의 {name} 은/는 등록할 수 없습니다.', end = '\n')
            return False
        else:
            print('이상 없습니다.', end = '\n')
            return True

create_user()


# 실습 4-5

from pprint import pprint as print
user_data = [
    {
        'blood_group': 'AB',
        'company': 'Stone Inc',
        'mail': 'ian17@yahoo.com',
        'name': 'Kathryn Jenkins',
        'website': [
            'https://www.boyd-herrera.com/',
            'https://watson.com/',
            'http://www.mitchell.com/',
            'http://irwin-cline.biz/',
        ],
    },
    {
        'blood_group': 'AB+',
        'company': 'Fleming Ltd',
        'mail': 'patricianelson@yahoo.com',
        'name': 'Angel Williamson',
        'website': [
            'https://wilson-johnson.com/',
            'https://santiago-hammond.com/',
            'https://morales.com/',
            'https://fry-fleming.com/',
        ],
    },
    {
        'blood_group': 'A+',
        'company': 'Scott PLC',
        'mail': 'lisajones@gmail.com',
        'name': 'Stephanie Herman MD',
        'website': ['https://www.boyer-stevens.org/', 'http://www.johnson.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Warren-Stewart',
        'mail': 'allisonjennifer@gmail.com',
        'name': 'Jon Martinez',
        'website': ['https://www.berg.com/'],
    },
    {
        'blood_group': 'AB+',
        'company': 'Fisher Inc',
        'mail': 'mross@yahoo.com',
        'name': 'Justin Brown',
        'website': [
            'https://www.gray.com/',
            'https://jones.com/',
            'http://williams.biz/',
            'https://hammond.net/',
        ],
    },
    {
        'blood_group': 'B-',
        'company': 'Pearson Group',
        'mail': 'gravesbarbara@hotmail.com',
        'name': 'Bobby Patterson',
        'website': ['https://www.cunningham.biz/', 'https://johnson.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'White, Andrade and Howard',
        'mail': 'mcole@gmail.com',
        'name': 'Michelle Strickland',
        'website': ['http://www.rose-gomez.com/', 'https://reilly.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Brown-Young',
        'mail': 'tmorales@hotmail.com',
        'name': 'Stephanie Moore',
        'website': ['https://schmidt.com/'],
    },
    {
        'blood_group': 'AB+',
        'company': 'Brooks PLC',
        'mail': 'wellsmatthew@hotmail.com',
        'name': 'Dr. David Johnson',
        'website': [
            'http://ford-dean.com/',
            'http://www.petersen.com/',
            'https://thompson-cooley.info/',
            'http://ryan-gay.com/',
        ],
    },
    {
        'blood_group': 'A-',
        'company': 'Stewart Group',
        'mail': 'sean37@hotmail.com',
        'name': 'Veronica Webb',
        'website': ['http://www.holmes.info/', 'http://www.morris.biz/'],
    },
    {
        'blood_group': 'AB+',
        'company': 'Cabrera, Perry and Harris',
        'mail': 'bgonzales@yahoo.com',
        'name': 'Lisa Wilcox',
        'website': ['https://www.small.com/', 'http://martin-petersen.com/'],
    },
    {
        'blood_group': 'B+',
        'company': 'Thomas, Lozano and Lopez',
        'mail': 'bperry@yahoo.com',
        'name': 'Brian Simmons',
        'website': [
            'http://reid.com/',
            'http://www.roman-neal.biz/',
            'https://www.hoover.org/',
            'https://www.lynn.com/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Baker-Leach',
        'mail': 'johnlucas@yahoo.com',
        'name': 'Carlos Robinson',
        'website': ['https://martin.com/', 'http://montgomery-cline.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Higgins, Higgins and Garcia',
        'mail': 'chris66@gmail.com',
        'name': 'Gabriel Collins',
        'website': ['https://www.cole-pugh.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Tanner, Wheeler and Weaver',
        'mail': 'leonardtammy@gmail.com',
        'name': 'Christopher Cook',
        'website': [
            'https://www.myers-reynolds.com/',
            'https://dunlap-rogers.com/',
            'https://luna.net/',
            'http://smith-miller.com/',
        ],
    },
    {
        'blood_group': 'A-',
        'company': 'Schaefer-Hunter',
        'mail': 'nsummers@gmail.com',
        'name': 'Daniel Monroe',
        'website': [
            'https://cook.net/',
            'http://carpenter.com/',
            'http://morris-terrell.com/',
        ],
    },
    {
        'blood_group': 'B+',
        'company': 'Stephens Group',
        'mail': 'rolson@gmail.com',
        'name': 'Molly Parks',
        'website': [
            'https://wright-vincent.biz/',
            'http://www.cruz.com/',
            'http://olson.org/',
            'http://gomez.com/',
        ],
    },
    {
        'blood_group': 'O-',
        'company': 'Fitzgerald, Costa and Hobbs',
        'mail': 'jennifervang@hotmail.com',
        'name': 'Jill Patterson',
        'website': [
            'https://www.brewer.com/',
            'https://malone-murray.info/',
            'http://evans.com/',
            'https://ortiz.com/',
        ],
    },
    {
        'blood_group': 'A-',
        'company': 'Frazier Ltd',
        'mail': 'vsolis@hotmail.com',
        'name': 'Marie May',
        'website': [
            'http://pratt.info/',
            'http://www.ortega.com/',
            'http://www.smith.net/',
            'https://nichols.biz/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Rodriguez and Sons',
        'mail': 'michael09@yahoo.com',
        'name': 'Julia Gonzalez',
        'website': [
            'https://www.cantrell.com/',
            'https://www.smith.net/',
            'http://delgado.com/',
            'http://stevens.com/',
        ],
    },
    {
        'blood_group': 'AB-',
        'company': 'Brown-Arnold',
        'mail': 'christopher79@hotmail.com',
        'name': 'David Garza',
        'website': ['https://price.net/'],
    },
    {
        'blood_group': 'A+',
        'company': 'Butler-Hernandez',
        'mail': 'angiechoi@yahoo.com',
        'name': 'Leslie Kemp',
        'website': ['http://www.martin-thompson.org/', 'http://martin.org/'],
    },
    {
        'blood_group': 'A-',
        'company': 'Schneider-Hensley',
        'mail': 'cesarsantos@hotmail.com',
        'name': 'Brandon Peterson',
        'website': [
            'https://www.owens-gay.com/',
            'https://www.santiago.org/',
            'https://www.singleton.com/',
        ],
    },
    {
        'blood_group': 'O-',
        'company': 'Hunter, Alvarado and Stewart',
        'mail': 'thomas16@gmail.com',
        'name': 'Matthew Stanley',
        'website': ['https://nelson.com/'],
    },
    {
        'blood_group': 'A+',
        'company': 'Elliott, Mullins and Michael',
        'mail': 'smithedward@hotmail.com',
        'name': 'Robert Brown',
        'website': ['http://montgomery-rogers.biz/', 'http://www.williams-nixon.com/'],
    },
    {
        'blood_group': 'AB+',
        'company': 'Velasquez-Garcia',
        'mail': 'samanthawilson@yahoo.com',
        'name': 'Stephanie Cohen',
        'website': ['http://jackson-harris.com/'],
    },
    {
        'blood_group': 'A+',
        'company': 'Mccoy-Hopkins',
        'mail': 'lli@yahoo.com',
        'name': 'Michael Clark',
        'website': [
            'https://www.harding.info/',
            'https://www.jones.biz/',
            'http://knight-adkins.org/',
            'http://www.alvarado-mendoza.org/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Kerr Ltd',
        'mail': 'georgebrittany@yahoo.com',
        'name': 'Brandon White',
        'website': ['https://flowers-parker.info/', 'http://oliver-rice.info/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Villarreal, Wood and Smith',
        'mail': 'denise73@yahoo.com',
        'name': 'Kevin Blevins',
        'website': [
            'http://www.ramirez.info/',
            'https://mckay.net/',
            'http://duran.com/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Jenkins-Garcia',
        'mail': 'kwoodward@hotmail.com',
        'name': 'Michelle Dixon',
        'website': [
            'http://www.taylor.com/',
            'https://bates-trujillo.org/',
            'https://www.thomas-boyer.org/',
        ],
    },
]

blood_types = ['A-', 'A+', 'B-', 'B+', 'O-', 'O+', 'AB-', 'AB+']
black_list = ['Jenkins-Garcia', 'Stephens Group', 'White, Andrade and Howard', 'Warren-Stewart']



def create_user(user_data):
    user_list = []
    False_count = 0
    for user_info in user_data:
        if is_validation(user_info) == 'blocked':
            False_count += 1
            continue

        elif is_validation(user_info)[0] == False:
            False_count += 1
            for wrong_data in is_validation(user_info)[1]:
                user_info[wrong_data] = None
        user_list.append(user_info)
    print(f'잘못된 데이터로 구성된 유저의 수는 {False_count}입니다.')
    return user_list
    

def is_validation(user_info):
    if user_info['company'] in black_list:
        return 'blocked'

    is_True = True
    result = []
    if user_info['blood_group'] not in blood_types:
        is_True = False
        result.append('blood_group')
    if '@' not in user_info['mail']:
        is_True = False
        result.append('mail')
    if len(user_info['name']) < 2 or len(user_info['name']) > 31:
        is_True = False
        result.append('name')
    if len(user_info['website']) <= 0:
        is_True = False
        result.append('website')
    return is_True, result

print(create_user(user_data))



# def create_user(user_data):
#     user_list = []
#     count = 0
#     for data in user_data:
#         result = is_validation(data)
#         if result == 'blocked':
#             count += 1
#             continue

#         elif result[0] == False:
#             count += 1
#             for wrong_data in result[1]:
#                 data[wrong_data] = None
#         user_list.append(data)
#     print(f'잘못된 데이터로 구성된 유저의 수는 {count} 입니다.')  
#     return user_list

# def is_validation(data):
#     if data['company'] in black_list:
#         return 'blocked'
    
#     check = True
#     check_list = []
#     if data['blood_group'] not in blood_types:
#         check = False
#         check_list.append('blood_group')
#     if '@' not in data['mail']:
#         check = False
#         check_list.append('mail')
#     if 2 > len(data['name']) or 31 < len(data['name']):
#         check = False
#         check_list.append('name')
#     if len(data['website']) <= 0:
#         check = False
#         check_list.append('website')

#     return check, check_list

# print(create_user(user_data))




# def validate_user_data(data):
#     blocked_users = []
#     invalid_users = []

#     for user in data:
#         if user['company'] in black_list:
#             blocked_users.append(user)
#         else:
#             valid, errors = is_valid_user(user)
#             if not valid:
#                 invalid_users.append((user, errors))

#     return blocked_users, invalid_users

# def is_valid_user(user):
#     errors = []

#     if user['blood_group'] not in blood_types:
#         errors.append('blood_group')
#     if '@' not in user['mail']:
#         errors.append('mail')
#     if len(user['name']) < 2 or len(user['name']) > 30:
#         errors.append('name')
#     if not user['website']:
#         errors.append('website')

#     return not errors, errors

# def create_user(user_data):
#     blocked_users, invalid_users = validate_user_data(user_data)
    
#     print(f'차단된 사용자: {json.dumps(blocked_users, indent=4)}')
#     print(f'잘못된 데이터로 구성된 사용자: {json.dumps(invalid_users, indent=4)}')

#     valid_users = [
#         {
#             key: user[key] if key not in errors else None
#             for key in user.keys()
#         }
#         for user, errors in invalid_users
#     ]

#     return valid_users

# print(create_user(user_data))







