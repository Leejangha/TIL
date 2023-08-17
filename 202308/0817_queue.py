from collections import deque
q = deque()
q.append('a')
q.append('b')
print(q)
print(q.popleft())
print(q.popleft())

from queue import PriorityQueue

q = PriorityQueue(maxsize=6)

# 추가
q.put(1)
q.put(2)
q.put(3)
q.put(4)

q.put((3, '윤태우'))
q.put((1, '황호철'))
q.put((2, '원종현'))
q.put((0, '허범성'))


print(q.get())
print(q.get())
print(q.get())
print(q.get())

p = 1 #줄설 '첫번째' 사람 번호

q = [] #큐
N = 20 #마이쮸 개수
m = 0 #나눠준 개수

while m < N:
    q.append((p, 1, 0))
    v, c, my = q.pop(0)
    print(f'큐에 남아있는 사람 수{len(q)+1} 받아갈 사탕수{c} 나눠준 사탕수{m}')

    m += c
    q.append((v, c+1, my+c))
    p += 1 #처음 줄서는 사람 번호
print(f'마지막 사랕을 받은 사람{v}')

# 1) 내장 모듈을 사용하여 바꾸기
# 2) 바꾼 코드를 마이쮸 개수를 늘려서 성능 테스트
