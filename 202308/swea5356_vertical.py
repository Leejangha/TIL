T = int(input())

for t in range(1, T+1):
    MAP = []
    max_len = 0
    for i in range(5):
        MAP.append(input())
        if len(MAP[i]) > max_len:
            max_len = len(MAP[i])
    for i in range(5):
        while len(MAP[i]) < max_len:
            MAP[i] += '_'
    lst = list(''.join(row) for row in list(zip(*MAP)))

    ans = ''
    for char in ''.join(lst):
        if char != '_':
            ans += char

    print(f'#{t} {ans}')


# 수정
T = int(input())

for t in range(1, T + 1):
    MAP = [input().ljust(15, '_') for _ in range(5)]
    lst = list(''.join(row) for row in zip(*MAP))
    ans = ''.join(char for char in ''.join(lst) if char != '_')

    print(f'#{t} {ans}')

#
for t in range(int(input())):
    STR = [input().ljust(15, '_') for _ in range(5)]
    string = list(zip(*STR))
    res = ''
    for s in string:
        for char in s:
            if char != '_':
                res += char

    print(f'#{t+1} {res}')
