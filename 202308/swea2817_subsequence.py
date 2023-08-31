def comb(i, visited, Sum):
    global cnt
    if Sum == K:
        cnt += 1
        return
    if i == N:
        return

    visited[i] = True
    comb(i+1, visited, Sum+A[i])
    visited[i] = False
    comb(i+1, visited, Sum)


for t in range(int(input())):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    visited = [False]*N
    cnt = 0
    comb(0, visited, 0)
    print(f'#{t+1} {cnt}')
