T = int(input())

for t in range(1, T+1):
    N = int(input())//10 - 1
    dp = [1, 3]

    for i in range(2, N + 1):
        dp.append(dp[i - 2] * 2 + dp[i - 1])
    print(f'#{t} {dp[N]}')
