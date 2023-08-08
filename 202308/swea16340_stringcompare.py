T = int(input())

for t in range(1, T+1):
    str1 = input()
    str2 = input()
    result = 0
    if str1 in str2:
        result = 1

    print(f'#{t} {result}')

# 삼항조건 연산자 사용
result = 1 if str1 in str2 else 0