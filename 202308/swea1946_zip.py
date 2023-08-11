T = int(input())

for t in range(1, T+1):
    string = ''
    N = int(input())
    for _ in range(N):
        C, K = input().split()
        string += C*int(K)
    print(f'#{t}')
    res = ''
    for i in range(len(string)):
        if len(res) < 10:
            res += string[i]
        else:
            print(res)
            res = ''
            res += string[i]
    print(res)
