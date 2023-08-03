T = int(input())

for t in range(1, T+1):
    N = int(input())
    sales = list(map(int, input().split()))

    now = 0
    next = 0
    profit = 0

    while now != N:
        next = sales.index(max(sales[now:]))
        if next == now:
            break
        profit += (sum(sales[now:next])*(-1) + max(sales[now:]) * (next-now))
        now = next + 1

    print(f'#{t} {profit}')


T = int(input())

for t in range(1, T+1):
    N = int(input())
    sales = list(map(int, input().split()))

    profit = 0
    sell_price = 0

    for price in sales[::-1]:
        if price >= sell_price:
            sell_price = price
        else:
            profit += sell_price - price

    print(f'#{t} {profit}')