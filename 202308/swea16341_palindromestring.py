T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    MAP = [list(input()) for _ in range(N)]

    palindrome = ''

    for i in range(N):
        for j in range(N-M+1):
            is_palin_row = 0
            is_palin_col = 0
            for k in range(M//2):
                if MAP[i][j+k] == MAP[i][j+M-k-1]:
                    is_palin_row += 1
                else:
                    is_palin_row = 0

                if MAP[j+k][i] == MAP[j+M-k-1][i]:
                    is_palin_col += 1
                else:
                    is_palin_col = 0

            if is_palin_row == M//2:
                for l in range(j, j+M):
                    palindrome += MAP[i][l]
            if is_palin_col == M//2:
                for l in range(j, j+M):
                    palindrome += MAP[l][i]

    print(f'#{t} {palindrome}')


# 수정
T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    MAP = [input() for _ in range(N)]
    MAP.extend([''.join(x) for x in zip(*MAP)])
    palindrome = ''

    for i in range(2*N):
        for j in range(N-M+1):
            is_palin= 1
            for k in range(M//2):
                if MAP[i][j+k] != MAP[i][j+M-k-1]:
                    is_palin = 0
                    break

            if is_palin == 1:
                palindrome = MAP[i][j:j+M]

    print(f'#{t} {palindrome}')
