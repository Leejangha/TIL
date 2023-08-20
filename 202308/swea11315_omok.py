d = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]

for t in range(int(input())):
    N = int(input())
    MAP = [input() for _ in range(N)]
    for x in range(N):
        for y in range(N):
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < N:

    print(f'#{t+1} {MAP}')