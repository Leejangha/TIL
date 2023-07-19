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

