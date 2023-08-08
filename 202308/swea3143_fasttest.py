T = int(input())

for t in range(1, T+1):
    A, B = map(str, input().split())
    cnt_B = A.count(B)

    res = len(A) - cnt_B * (len(B)-1)
    print(f'#{t} {res}')
