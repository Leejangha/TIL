for i in range(10):
    N = int(input())
    heights = list(map(int, input().split()))
    sum_sights = 0
    for j in range(2, N-1):
        sights = []
        if heights[j] == max(heights[j-2:j+3]):
            for k in [-2, -1, 1, 2]:
                sights.append((heights[j] - heights[j+k]))
            sum_sights += min(sights)
 
    print(f'#{i+1} {sum_sights}')