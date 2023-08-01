T = int(input())
 
for i in range(T):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    sum_list = []
    for j in range(N-M+1):
        sum_list.append(sum(numbers[j:j+M]))
    print(f'#{i+1} {max(sum_list) - min(sum_list)}')