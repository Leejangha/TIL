def rotate_array(arr):
    n = len(arr)
    rotated = [[0] * n for _ in range(n)]
 
    for i in range(n):
        for j in range(n):
            rotated[j][n-1-i] = arr[i][j]
     
    return rotated
 
T = int(input())
 
for i in range(T):
    N = int(input())
    row = [list(map(int, input().split())) for _ in range(N)]
 
    rotated_90 = rotate_array(row)
    rotated_180 = rotate_array(rotated_90)
    rotated_270 = rotate_array(rotated_180)
 
    print('#{}'.format(i+1))
    for i in range(N):
        print(''.join(map(str, rotated_90[i])), ''.join(map(str, rotated_180[i])), ''.join(map(str, rotated_270[i])))