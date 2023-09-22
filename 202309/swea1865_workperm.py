def perm(n, rate):
    global max_rate
    if n == N:
        max_rate = max(rate, max_rate)
        return
    if rate < max_rate:
        return

    for i in range(N):
        if not used[i] and input_list[n][i] != 0:
            used[i] = 1
            perm(n+1, rate*input_list[n][i]*0.01)
            used[i] = 0


for t in range(int(input())):
    N = int(input())
    input_list = [list(map(int, input().split())) for _ in range(N)]
    max_rate = 0
    used = [0] * N
    perm(0, 100)
    print(f'#{t+1} {max_rate:.6f}')