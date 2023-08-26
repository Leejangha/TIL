for t in range(int(input())):
    N = int(input()) + 1
    deck = list(input().split())
    perfect = []
    for i in range(N//2):
        perfect.append(deck[i])
        if N//2+i < N-1:
            perfect.append(deck[N//2+i])
    print(f'#{t+1}', *perfect)
