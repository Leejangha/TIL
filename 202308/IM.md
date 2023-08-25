차르봄바

```python
dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1] #direct + x,y (방향 배열, 델타탐색 -> x값이 감소되면 "행"이 변함

T = int(input())

for t in range(1, T + 1):
    N, P = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    for i in range(N):
        for j in range(N):
            cnt = MAP[i][j]
            for d in range(4):
                for k in range(1, P + 1):
                    ny = i + dx[d] * k
                    nx = j + dy[d] * k
                    if ny < 0 or nx < 0 or ny >= N or nx >= N:
                        continue
                    cnt += MAP[ny][nx]
            result = max(cnt, result)

    print(f"#{t} {result}")
```

사각형 그리기 게임

```python
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    maxarea = 0
    result = 0

    for x in range(N):
        for y in range(N):
            cur = MAP[x][y]

            for nx in range(x, N):
                for ny in range(y, N):
                    if MAP[nx][ny] == cur:
                        area = (nx - x + 1) * (ny - y + 1)
                        if area > maxarea:
                            maxarea = area
                            result = 1
                        elif area == maxarea:
                            result += 1

    print(f"#{t} {result}")
```

Captcha Code

```python
T = int(input())
for tc in range(1, T+1) : 
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))
    
    indexes = [] 
    res = 1 
    
    for i in range(len(passcode)) : 
        now = passcode[i]
        try : 
            index = sample.index(now)
            sample = sample[index:]
        except : 
            res = 0 

    print(f"#{tc} {res}")
```

답안지 채점

```python
T = int(input())

for t in range(1,T+1):
    N, M = map(int,input().split())
    answer = list(map(int,(input().split())))
    student = []
    score = []
    for i in range(N):
        student.append(list(map(int,(input().split()))))

    for i in range(len(student)):
        cnt = 0
        result = 0
        for j in range(len(answer)):

            if student[i][j] == answer[j]:
                cnt += 1
                result += cnt
            else :
                cnt = 0
        score.append(result)
    
    result = max(score) - min(score)

    print(f"#{t} {result}")
```

중계기

```python
T = int(input())

for t in range(1,T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N + 1)]
    repeater = ()


    def findRepeater():

        for i in range(N + 1):
            for j in range(N + 1):
                if MAP[i][j] == 2:
                    return i, j


    def findDistant(i, j):
        sqrt = []

        for hi in range(N + 1):
            for hj in range(N + 1):
                if MAP[hi][hj] == 1:
                    sqrt.append((abs(hi - i) ** 2) + abs(hj - j) ** 2)

        return max(sqrt)


    repeater = findRepeater()
    value = findDistant(repeater[0], repeater[1])

    # 입력 n 이있을때, 최대거리는 (n-0)**2 + (n-0)**2이다.
    # 현재 문제에서는 최대 n이 10이였으므로, 100+100 -> 제곱해서 200이 되는수보단 작다
    # 15*15를 하면, 225로 유효범위를 넘을 수 있다
    for i in range(15):
        if i ** 2 >= value:
            print(f"#{t} {i}")
            break
```

