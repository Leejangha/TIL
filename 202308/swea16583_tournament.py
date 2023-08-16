def rsp(i, j):
    if cards[i] == cards[j]:
        return i
    elif (cards[i],cards[j]) in [(1,3), (2,1), (3,2)]:
        return i
    else:
        return j


def tournament(i, j):
    if i == j:
        return i
    mid = (i + j) // 2
    win1 = tournament(i, mid)
    win2 = tournament(mid + 1, j)
    return rsp(win1, win2)


for t in range(int(input())):
    N = int(input())
    cards = list(map(int, input().split()))
    res = tournament(0,N-1)+1

    print(f'#{t + 1} {res}')
