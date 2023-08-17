for t in range(int(input())):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    corridor = [0] * 200
    for x,y in MAP:
        if x < y:
            for i in range((x-1)//2, (y-1)//2+1):
                corridor[i] += 1
        else:
            for i in range((y-1)//2, (x-1)//2+1):
                corridor[i] += 1
    res = max(corridor)
    print(f'#{t+1} {res}')
