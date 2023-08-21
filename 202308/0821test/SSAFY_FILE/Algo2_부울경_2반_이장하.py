T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    # 카드덱
    cards_A = list(map(str, input().split()))
    # 홀수, 큐
    cards_B = []
    # 짝수, 스택
    cards_C = []

    bonus = 0

    for char in cards_A:
        # 더하기 카드가 나올때 마다 보너스 숫자 + 1
        if char == '+':
            bonus += 1
        # 더하기 카드가 아닌경우 숫자 카드이므로
        else:
            # A 덱에서 뽑은카드에 보너스를 더한 카드를
            card = int(char) + bonus
            # 짝수일 경우 C에 넣는다
            if card % 2 == 0:
                cards_C.append(card)
            # 홀수일 경우 B에 넣는다
            else:
                cards_B.append(card)
    # 각 참가자의 점수를 리스트에 넣는다
    point = []
    # B 또는 C에 카드가 남아 있는 동안
    while cards_B or cards_C:
        # B에 있는 카드를 앞에서 부터 가져간다.
        if cards_B:
            point_B = cards_B.pop(0)
        # 카드가 없는 경우 0점
        else:
            point_B = 0
        # C에 있는 카드를 뒤에서 부터 가져간다.
        if cards_C:
            point_C = cards_C.pop()
        # 카드가 없는 경우 0점
        else:
            point_C = 0
        # B와 C에서 가져온 카드의 합이 점수가 된다.
        point.append(point_B + point_C)
    # 가져온 카드가 없는 경우 0점
    res = 0
    # 김싸피가 점수를 얻은 경우
    if len(point) > (M-1):
        res = point[M-1]

    print(f'#{t} {res}')
