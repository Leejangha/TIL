for t in range(int(input())):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    for i in range(M):
        queue.append(queue.pop(0))
    print(f'#{t+1} {queue[0]}')
