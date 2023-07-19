# Functions
def greet(name):
    """입력된 이름 값에
    인사를 하는 메세지를 만드는 함수
    """
    message = 'Hello, ' + name
    return message

result = greet('Alice')
print(result)

# parameter, argument
def add_numbers(x, y): # x와 y는 매개변수
    result = x + y
    return result

a = 2
b = 3
sum_result = add_numbers(a, b) # a와 b는 인자
print(sum_result)


# Positional Arguments (위치인자)
def greet(name, age = 30): # 30 = Default Argument Values(기본 인자 값)
    print('안녕하세요, {}님! {}살이시군요.'.format(name, age))

greet('Bob') # 안녕하세요, Bob님! 30살이시군요.
greet('Charlie', 40) # 안녕하세요, Charlie님! 40살이시군요.


# Keyword Arguments (키워드 인자)
def greeting(name, age):
    print('안녕, {}, {}!!'.format(name, age))

greeting('Alice', 25) # 안녕, Alice, 25!!

greeting(25, 'Alice') # 안녕, 25, Alice!!

greeting(age = 25, name = 'Alice') # 안녕, Alice, 25!!


# Arbitrary Arguments Lists (임의의 인자 목록)
def calculate_sum(*args):
    print(args) # (1, 2, 3, 4, 5)

calculate_sum(1, 2, 3, 4, 5)


# Arbitrary Keyword Arguments Lists (임의의 키워드 인자 목록)
def calculate_sum(**kwargs):
    print(kwargs) # {'name': 'Alice', 'age': 30, 'address': 'Korea'}

calculate_sum(name = 'Alice', age = 30, address = 'Korea')

# 함수의 인자 권장 작성순서
print('hello', end = ' ')
print('asdasd')


# Python의 범위(Scope)

# 이름 검색 규칙
print(sum([1, 2, 3]))

# 재귀 함수

# 팩토리얼
def factorial(n):
    # 종료 조건 : n이 0이면 1을 반환
    if n == 0:
        return 1
    # 재귀 호출 : n에 n - 1의 팩토리얼을 곱한 결과를 반환
    return n * factorial(n - 1)

# 팩토리얼 계산 예시
result = factorial(5)
print(result)


# map



numbers = [1, 2, 3]
result = map(str, numbers)

print(result)
print(list(result))

result = []
for number in numbers:
    result.append(str(number))


numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x*2, numbers))
print(result)


# scope

a = 1 #global

def test():
    c = 1 #local
    print(c)

test()
print(c)

# LEGB
print(sum)

sum = 10 #built-in
a = 1
print(sum) #10

def test():
    sum = 11
    print(sum)
    print(a)
test()


(10, 2, 500) # local
(10, 2, 3) # enclosed
(1, 2) # global


def test():
    test()

test()

def fac(n):
    if n == 0:
        return 1
    
    return n * fac(n-1)

fac(3)


# zip

a = [1, 2, 3]
b = [4, 5, 6]
c = zip(a,b)

print(c)
print(list(c))


# lambda(익명 함수)

def test(n):
    return n * 2

test(2)

def addition(x, y):
    return x + y

result = addition(3, 5)
print(result)

addition = lambda x, y: x + y

result = addition(3, 5)
print(result)


# Packing & Unpacking

packed_values = 1, 2, 3, 4, 5
print(packed_values) #(1, 2, 3, 4, 5)


numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers

print(a) # 1
print(b) # [2, 3, 4]
print(c) # 5


lst = [1, 2, 3]
a, b, c = lst

print(a)
print(b)
print(c)

print('1 2 3')
results = [1, 2, 3]
print(results)

for result in results:
    print(result, end = " ")

print()

print(*results)
############## 상단 이터러블 언패킹 하단 non 이터러블 언패킹

def test(a, b, c):
    print(a, b, c)

dic = {'a' : 1, 'b' : 2, 'c' : 3}
test(**dic)

print(dic)
print(*dic)
print(**dic)

import math

print(math.pi)

print(math.sqrt(4))

