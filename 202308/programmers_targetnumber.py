def solution(numbers, target):
    answer = 0
    return answer

T = int(input())

for t in range(T):
    numbers = list(map(int, input().split()))
    target = int(input())

    print(f'#{t} {solution(numbers, target)}')
