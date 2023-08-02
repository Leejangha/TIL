T = int(input())

for t in range(1, T+1):
    N = int(input())
    sales = list(map(int, input().split()))

    now = 0
    next = 0
    profit = 0

    while next != N:
        next = sales.index(max(sales[now:]))
        print(next)
        if next == now:
            break
        profit += (sum(sales[now:next-1])*(-1) + max(sales[now:]) * (next-now))
        now = next

    print(f'#{t} {profit}')