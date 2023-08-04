T = int(input())

for t in range(1, T+1):
    D, A, B, F = map(int, input().split())
    T = D/(A+B)
    l = T*F
    print(f'#{t} {l}')