num = int(input('숫자를 입력하세요 : '))

# if statement
# num이 홀수라면
if num % 2 == 1:
# if num % 2: # if에서 1이 True
    print('홀수입니다.')
# num이 홀수가 아니라면(짝수면)
else:
    print('짝수입니다.')


# 학점 계산기
score = 70

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')


# for statement
# for 변수 in iterable
for n in 1, 2, 3: # tuple로 인식
    print(n)


num_lists = [1,2,3]

for num_list in num_lists:
    print(num_list * 2)


# 인덱스로 리스트 순회
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)


# 중첩 반복문
paddings = [3,7]
outers = [8,3,5]
inners = [5,3,8,5]
for padding in paddings:
    for outer in outers:
        for inner in inners:
            print(padding, outer,inner)




# 0~9 요소를 가지는 리스트 만들기 (1~10)
# 1. 일반적인 방법
arr = []
for i in range(10):
    if i % 2 == 1:
        arr.append(i)
print(arr)

# List Comprehension
arr_2 = [i for i in range(10) if i % 2 == 1]
arr_3 = [i if i % 2 == 1 else str(i) for i in range(10)]
print(arr_2)
print(arr_3)


num_lists = [1,2,3]

a = [num_list + 1 for num_list in num_lists]

b = list(num_list + 1 for num_list in num_lists)

print(a)
print(b)

SET = {i + 1 for i in range(5)}
print(SET)

TUPLE  = tuple(i + 1 for i in range(5))
print(TUPLE)

odd = [i + 1 for i in range(5) if i % 2 == 1]
print(odd)


lst = ['1',1,'가']
T = (1,2,3)

for l in enumerate(lst):
    print(l)

for index, l in enumerate(T):
    print(f'{index}')
    
for index, l in enumerate(T, start = 1):
    print(f'{index}번째 원소는 {l}')




# 리스트를 생성하는 3가지 방법 비교
# 어떤게 제일 빨라요??

numbers = ['1', '2', '3']

# 1. for loop
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)

# 2. map
new_numbers_2 = list(map(int, numbers))
print(new_numbers_2)

# 3. list comprehension
new_numbers_3 = [int(number) for number in numbers ]
print(new_numbers_3)

fruits = ['a', 'b', 'c']

for index, fruit in enumerate(fruits):
    print(f'인데스 {index}: {fruit}')

print(enumerate(fruits))
print(list(enumerate(fruits)))

for index, elem in enumerate(fruits):
    print(index, elem)


