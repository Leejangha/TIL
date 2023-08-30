def find_path(lst, visited, sum_len):
    global min_len
    if len(lst) == N:
        sum_len += abs(MAP[0]-MAP[lst[0]*2+4])+abs(MAP[1]-MAP[lst[0]*2+5])+abs(MAP[2]-MAP[lst[-1]*2+4])+abs(MAP[3]-MAP[lst[-1]*2+5])
        for i in range(N-1):
            start = lst[i]*2 + 4
            next = lst[i+1]*2 + 4
            sum_len += abs(MAP[start]-MAP[next])+abs(MAP[start+1]-MAP[next+1])
            if sum_len > min_len:
                break
        if min_len > sum_len:
            min_len = sum_len
        return
    for i in range(N):
        if not visited[i]:
            lst.append(i)
            visited[i] = True
            find_path(lst, visited, sum_len)
            visited[i] = False
            lst.pop()


for t in range(int(input())):
    N = int(input())
    MAP = list(map(int, input().split()))
    lst = []
    min_len = float('inf')
    visited = [False] * N
    find_path(lst, visited, 0)
    print(f'#{t+1} {min_len}')
