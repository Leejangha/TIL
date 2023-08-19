T = int(input())

for t in range(1, T+1):
    N = int(input())
    dp = [1, 2, 4]

    for i in range(3, N):
        dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])
    print(dp[N-1])
