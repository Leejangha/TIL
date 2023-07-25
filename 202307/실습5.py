# 실습 5-1

# 아래 함수를 수정하시오.
def reverse_string(string):
    return "".join(reversed(string))

# test 
def reverse_string(string):
    result = ''
    for char in string:
        result = char + result
    return result

result = reverse_string("Hello, World!")
print(result)


# 실습 5-2

# 아래 함수를 수정하시오.
def remove_duplicates(lst):
    new_lst = []
    new_lst = list(set(lst))
    return new_lst

# test
def remove_duplicates(lst):
    new_lst = []

    for l in lst:
        if l not in new_lst:
            new_lst.append(l)

    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)


# 실습 5-3

# 아래 함수를 수정하시오.
def sort_tuple(arr):
    return tuple(sorted(arr))

# test
def sort_tuple(t):
    new_tuple = ()

    sort_lists = sorted(t)
    for sort_list in sort_lists:
        new_tuple += (sort_list,)

    return new_tuple

result = sort_tuple((5, 2, 8, 1, 3))
print(result)


# 실습 5-4

# 아래 함수를 수정하시오.
def capitalize_words(string):
    return string.title()

# test
def capitalize_words(string):
    return

result = capitalize_words("hello, world!")
print(result)


# 실습 5-5

# 아래 함수를 수정하시오.
def even_elements(lst):
    arr = []
    arr.extend(lst)
    i = 0
    while i < len(arr):
        if arr[i] % 2 == 1:
            arr.pop(i)
        else:
            i += 1
    return arr

# test
def even_elements(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result

def even_elements(numbers):
    result = []
    while numbers:
        number = numbers.pop(0)
        if number % 2 == 0:
            result.extend([number])
    return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)


# 과제 5-2

# 아래 함수를 수정하시오.
def count_character(x, y):
    result = x.count(y)
    return result

# test
def count_character(string, character):
    count = 0
    for s in string:
        if s == character:
            count += 1
    return count

result = count_character("Hello, World!", "o")
print(result) # 2


# 과제 5-4

# 아래 함수를 수정하시오.
def find_min_max(lst):
    M = max(lst)
    m = min(lst)
    return m, M

# test
def find_min_max(numbers):
    min_value = numbers[0]
    max_value = numbers[0]

    for number in numbers:
        if min_value > number:
            min_value = number
        
        if number > max_value:
            max_value = number
    
    return min_value, max_value


result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)



# test ex

scores = [85, 90, 100]
sum = 0
len = 0

for score in scores:
    sum += score
    len += 1
mean = sum / len

print(mean)