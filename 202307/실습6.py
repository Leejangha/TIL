# 실습 6-1

# 아래 함수를 수정하시오.
def union_sets(x, y):
    return x.union(y)

result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)


# 실습 6-2

# 아래 함수를 수정하시오.
def get_value_from_dict(x, y):
    return x.get(y)

my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result) # Alice


# 실습 6-3

# 아래 함수를 수정하시오.
def intersection_sets(x, y):
    return x.intersection(y)

result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result) # {3}


# 실습 6-4

# 아래 함수를 수정하시오.
def get_keys_from_dict(x):
    key_list = []
    for k in x.keys():
        key_list.append(k)
    return key_list

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)


# 실습 6-5

# 아래 함수를 수정하시오.
def difference_sets(x, y):
    return x.difference(y)

result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)


# 과제 6-2

def remove_duplicates_to_set(x):
    return set(x)

		
result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)


# 과제 6-4

# 아래 함수를 수정하시오.
def add_item_to_dict(x, y, z):
    new_dict = x.copy()
    new_dict.setdefault(y , z)
    return new_dict

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
