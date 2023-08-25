code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

for t in range(int(input())):
    N, M = map(int, input().split())
    lst = [input() for _ in range(N)]
    for l in lst:
        if '1' in l:
            Cipher = l

    for i in range(M-1,0,-1):
        if Cipher[i] == '1':
            idx = i
            Cipher = Cipher[idx - 55:idx + 1]
            break

    Pass = []
    for i in range(8):
        Pass.append(code[Cipher[i*7:(i+1)*7]])

    cnt = 0
    for i in range(0,8,2):
        cnt += Pass[i]*3
        cnt += Pass[i+1]

    res = 0
    if cnt % 10 == 0:
        res = sum(Pass)
    print(f'#{t+1} {res}')
 