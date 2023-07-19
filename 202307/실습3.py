# 실습 3-1

number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1
    return number_of_people


increase_user()
print('현재 가입 된 유저 수 : {}'.format(number_of_people))


# 실습 3-2

number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1
    pass

def create_user():
    print('현재 가입 된 유저 수 : {}'.format(number_of_people))
    increase_user()
    user = ['홍길동', 30, '서울']
    user_info = {'name' : user[0], 'age' : user[1], 'address' : user[2]}
    print('{}님 환영합니다!'.format(user_info['name']))
    print(user_info)
    print('현재 가입 된 유저 수 : {}'.format(number_of_people))
    pass

create_user()


# 실습 3-3

# book.py
number_of_book = 100

def decrease_book(N):
    global number_of_book
    for i in range(N):
        number_of_book -= 1
    print('남은 책의 수 : {}'.format(number_of_book))
    pass

# ws_3_3.py
def rental_book(name, N):
    decrease_book(N)
    print('{}님이 {}권의 책을 대여하였습니다.'.format(name, N))
    pass

rental_book('홍길동', 3)

# 실습 3-4

number_of_people = 0


def increase_user():
    global number_of_people
    for i in range(len(name)):
        number_of_people += 1
    return

def create_user(n, a, ad):
    increase_user()
    user_info = {'name' : n, 'age' : a, 'address' : ad}
    print('{}님 환영합니다!'.format(user_info['name']))
    return user_info

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

user_info_list = list(map(create_user, name, age, address))
print(user_info_list)


# 실습 3-5

number_of_people = 0


def increase_user():
    global number_of_people
    for i in range(len(name)):
        number_of_people += 1
    pass


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(n, a, ad):
    increase_user()
    user_info = {'name' : n, 'age' : a, 'address' : ad}
    print('{}님 환영합니다!'.format(user_info['name']))
    return user_info


many_user = None
info = list(map(create_user, name, age))

# book.py
number_of_book = 100

def decrease_book(N):
    global number_of_book
    for i in range(N):
        number_of_book -= 1
    print('남은 책의 수 : {}'.format(number_of_book))
    pass

def rental_book(info):
    
    decrease_book(info['age']//10)
    pass


# 과제 3-2

def add_numbers(x, y):
    sum_result = x + y
    print("{}와 {}를 인자로 넘긴 경우, \n{}".format(x, y, sum_result))
    pass

#수정한 add_numbers() 함수를 호출하시오.
add_numbers(3, 5)


# 과제 3-4

