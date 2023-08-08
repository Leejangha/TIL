T = int(input())

dict_num = {
        "ZRO": 0,
        "ONE": 1,
        "TWO": 2,
        "THR": 3,
        "FOR": 4,
        "FIV": 5,
        "SIX": 6,
        "SVN": 7,
        "EGT": 8,
        "NIN": 9
    }
dict_num_list = list(dict_num)

for t in range(1, T+1):
    tc, N = map(str, input().split())
    N = int(N)
    string = list(input().split())

    arr = []
    for char in string:
        arr.append(dict_num[char])
    arr.sort()

    result = []
    for num in arr:
         result.append(dict_num_list[num])

    print(f'{tc}')
    for char in result:
        print(char, end=" ")
    print()


# 코드 수정
T = int(input())

dict_num = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4,
            "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

for t in range(1, T+1):
    tc, N = input().split()
    string = input().split()

    arr = []
    for char in dict_num:
        arr.append(string.count(char)) 

    print(f'{tc}')
    for i, j in dict_num.items():
        print((i+' ') * arr[j], end=" ")
    print()

# 풀이
target = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for _ in range(int(input())):
    num, lst = map(str, input.split())
    str_list = list(map(str, input.split()))
                    
    for i in range(10):
        cnt = 0
        for STR in str_list:
            if str == target[i]:
            cnt += 1

        result += target[i] * cnt

    print(num)
    print()