for t in range(int(input())):
    N = int(input())
    lst = []
    for _ in range(N):
        s, e = map(int, input().split())
        lst.append((s, e))
    lst.sort(key=lambda x: x[1])
    res = 0
    end = 0
    for i in range(N):
        start = lst[i][0]
        if start >= end:
            res += 1
            end = lst[i][1]
    print(f'#{t+1} {res}')
