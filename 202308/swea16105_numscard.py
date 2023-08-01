T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int,input()))
    max_num = 0
    counts = [0]*10
    for i in range(10):
        counts[i] = numbers.count(i)
        if counts[i] >= numbers.count(max_num):
            max_num = i
    print(f'#{t} {max_num} {counts[max_num]}')