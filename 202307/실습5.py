# 실습 5-1

# 아래 함수를 수정하시오.
def reverse_string(str):
    rev = str[::-1]
    return rev
    
result = reverse_string("Hello, World!")
print(result)


# 실습 5-2

# 아래 함수를 수정하시오.
def remove_duplicates(lst):
    new_lst = []
    new_lst = list(set(lst))
    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)


# 실습 5-3

# 아래 함수를 수정하시오.
def sort_tuple(arr):
    new_tuple = tuple(sorted(arr))
    return new_tuple

result = sort_tuple((5, 2, 8, 1, 3))
print(result)


# 실습 5-4

# 아래 함수를 수정하시오.
def capitalize_words(str):
    return str.title()

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


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)


# 과제 5-2

# 아래 함수를 수정하시오.
def count_character(x, y):
    result = x.count(y)
    return result

result = count_character("Hello, World!", "o")
print(result) # 2


# 과제 5-4

# 아래 함수를 수정하시오.
def find_min_max(lst):
    M = max(lst)
    m = min(lst)
    return m, M

result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)
