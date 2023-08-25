code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

for t in range(int(input())):
    N, M = map(int, input().split())
    lst = [bin(int(input().strip(), 16))[2:] for _ in range(N)]
    Cipher = list(set(lst))
    Cipher.remove('0')
    n = len(Cipher)
    # Code = [[0] for _ in range(n)]
    for i in range(n):
        Cipher[i] = '0'*(56-n%56) + Cipher[i]
        for j in range(len(Cipher[i])-1,0,-1):
            if Cipher[i][j] == '1':
                idx = j
                l = idx//56
                Cipher[i] = Cipher[i][idx-(56*l-1):idx+1:l]
                break
    l = len(Cipher)
    Pass = [[] for _ in range(l)]
    res = []
    for i in range(l):
        C = Cipher[i]
        for j in range(8):
            if C[j*7:(j+1)*7] in code:
                Pass[i].append(code[C[j*7:(j+1)*7]])
            else:
                continue
        cnt = 0
        K = len(Pass[i])
        k = 0
        while k < K-1:
            cnt += Pass[i][k] * 3
            cnt += Pass[i][k+1]
            k += 2
        if cnt % 10 == 0 and cnt != 0:
            res.append(sum(Pass[i]))

    print(f'#{t+1} {sum(res)}')

# 강사님 코드
hex_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
}

DICT = {
    '211': 0, '221': 1, '122': 2, '411': 3, '132': 4,
    '231': 5, '114': 6, '312': 7, '213': 8, '112': 9
}


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [input().strip() for _ in range(N)]
    SET = set(lst)
    result = set()
    newSet = set()

    for s in SET:
        if not all(char == '0' for char in s):
            newSet.add(s)

    for ns in newSet:
        binaryString = ''
        for char in ns:
            binaryString += hex_bin[char]

        start = 0
        countArray = []
        for i in range(len(binaryString)):
            if binaryString[i] != binaryString[start]:
                countArray.append(i - start)
                start = i

        pwd = []
        for i in range(1, len(countArray), 4):
            mn = min(countArray[i:i+3])
            key = str(countArray[i]//mn) + str(countArray[i+1]//mn) + str(countArray[i+2]//mn)
            pwd.append(DICT[key])

        for i in range(0, len(pwd), 8):
            result.add(tuple(pwd[i:i+8]))

    res = 0
    for r in result:
        if (sum(r[0:8:2]) * 3 + sum(r[1:8:2])) % 10 == 0:
            res += sum(r)

    print(f'#{t} {res}')
