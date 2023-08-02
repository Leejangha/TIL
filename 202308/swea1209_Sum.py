for _ in range(10):
    t = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    Max = 0
    for i in range(100):
        sum_row = 0
        sum_col = 0
        sum_dia = 0
        sum_dia2 = 0
        for j in range(100):
            sum_row += arr[i][j]
            sum_col += arr[j][i]
            if i == j:
                sum_dia += arr[j][i]
            elif i + j == 99:
                sum_dia2 += arr[j][i]
        if sum_row >= Max:
            Max = sum_row
        if sum_col >= Max:
            Max = sum_col
        if sum_dia >= Max:
            Max = sum_dia
        if sum_dia2 >= Max:
            Max = sum_dia2
    print(f'#{t} {Max}')