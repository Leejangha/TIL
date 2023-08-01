T = int(input())
 
for t in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(f'#{t+1} {max(numbers) - min(numbers)}')