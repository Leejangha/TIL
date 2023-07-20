# 진법 변경
print(bin(12))
print(oct(12))
print(hex(12))

print(2 / 3)
print(5 / 3)

# 지수(제곱하는 횟수) 표현 10^
print(314e-2)


# f-string
bugs = 'roaches'
counts = 13
area = 'living room'
print(f'Debugging {bugs} {counts} {area}')
print('Debugging {} {} {}'.format(bugs, counts, area))
print('Debugging %s %d %s' % (bugs, counts, area))


# f-string 응용
greeting = 'hi'
print(f'{greeting:>10}')


# slicing
my_str = [0, 1, 2, 3, 4]

print(my_str[2:4])
print(my_str[:3])
print(my_str[0:5:2])
print(my_str[::1])
print(my_str[::-1])


# 세트 표현

# 불변과 가변
my_str = 'hello'
my_str[0] = 'z'

my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)


# collection

name = "이장하"
age = 25

print("나는 {}입니다 {}살 입니다".format(name, age))


# 암시적 형변환
print(3 + 5.0) # 8.0
print(True + 3) # 4
print(True + False) # 1


# 명시적 형변환
print(int('1')) # 1
print(str(1) + '등') # 1등
print(float('3.5')) # 3.5
print(int(3.5)) # 3
print(int('3.5')) # error


# 비교 연산자
print(3 > 6) # False
print(2.0 == 2) # True
print(2 != 2) # False
print('HI' == 'hi') # False
# ==은 값(데이터)를 비교하지만 is는 주소(레퍼선스)를 비교한다
print(2.0 is 2) # False


# 논리 연산자
print(True and False) # False
print(True or False) # True
print(not True) # False
print(not 0) # True

# 단축평가
print(3 and 5)
print(False and 5)
print(5 and False)
print(5 and 3)
print(3 and 0)
print(0 and 3)
print(0 and 0)

print(5 or 3)
print(3 or 0)
print(0 or 3)
print(0 or 0)

vowels = 'aeiou'

print(('a' and 'b') in vowels)
print(('b' and 'a') in vowels)


# 멤버쉽 연산자
word = 'hello'
numbers = [1, 2, 3, 4, 5]

print('h' in word) # True
print('z' in word) # False

print(4 not in numbers) # False
print(6 not in numbers) # True