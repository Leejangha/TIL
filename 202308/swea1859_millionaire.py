T = int(input())

for t in range(1, T+1):
    # 날짜 입력
    N = int(input())
    # 매매가 입력
    sales = list(map(int, input().split()))

    # 변수 설정
    now = 0
    next = 0
    profit = 0

    # 날짜가 N일이 될때까지
    while now != N:
        # 다음 날짜 계산
        next = sales.index(max(sales[now:]))
        # 오늘이 최대가인 경우 중지
        if next == now:
            break
        # 이익 계산
        profit += (sum(sales[now:next])*(-1) + max(sales[now:]) * (next-now))
        # 오늘을 다음날로
        now = next + 1

    print(f'#{t} {profit}')


T = int(input())

for t in range(1, T+1):
    # 날짜 입력
    N = int(input())
    # 매매가 입력
    sales = list(map(int, input().split()))

    # 변수 설정
    profit = 0
    sell_price = 0

    # 매매가를 마지막 날부터 역순으로 대입
    for price in sales[::-1]:
        # 최대 매매가 갱신
        if price >= sell_price:
            sell_price = price
        else:
            # 이익 계산
            profit += sell_price - price

    print(f'#{t} {profit}')