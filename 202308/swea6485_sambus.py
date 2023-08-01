T = int(input())

for t in range(1, T+1):
    N = int(input())
    lines = [0] * 5001
    for i in range(N):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            lines[j] += 1
    P = int(input())
    result = []
    for i in range(P):
        num = int(input())
        result.append(lines[num])
    print(f'#{t}', *result)