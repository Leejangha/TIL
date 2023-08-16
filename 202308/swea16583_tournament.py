def rsp(i,j):
    if abs(i-j) == 1:
        return max(i, j)
    if abs(i-j) == 2:
        return min(i, j)
    if abs(i-j) == 0:
        return i

def tournament(i, j, a):
    mid = (i+j)//2
    if len(a) == 1:
        return
    if len(a) == 2:
        win_idx = a.index(rsp(a[0]a[1]))
        return

    if mid % 2 == 1:
        win_idx = tournament(0, mid, a[:mid])
        win2_idx = tournament(mid, j, a[mid:])+mid
    else:
        win_idx = a.index(rsp(a[:mid]))
        win2_idx = a[mid:].index(rsp(a[mid:])) + mid

    return tournament(0,)


for t in range(int(input())):
    N = int(input())
    cards = list(map(int, input().split()))
    tournament(0, N-1, cards)


    print(f'#{t+1} {win}')