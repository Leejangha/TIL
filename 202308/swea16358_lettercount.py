T = int(input())

for t in range(1, T+1):
    str1 = input()
    str2 = input()

    # 딕셔너리에 str1의 글자와 str2안에 있는 개수를 저장
    dict1 = {}
    for char in str1:
        dict1[char] = str2.count(char)  
    # DICT = dict.fromkeys(str1, 0)

    # 가장 많은 글자의 개수 계산
    max_val = 0
    for val in dict1.values():
        if val > max_val:
            max_val = val

    print(f'#{t} {max_val}')
