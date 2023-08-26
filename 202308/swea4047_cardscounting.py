for t in range(int(input())):
    deck = {'S': [], 'D': [], 'H': [], 'C': []}
    cards = list(input())
    res = True
    for i in range(0, len(cards), 3):
        T = cards[i]
        XY = cards[i+1]+cards[i+2]
        if XY not in deck[T]:
            deck[T].append(XY)
        else:
            res = False

    print(f'#{t+1}', end=' ')
    if res:
        for i in deck.keys():
            print(13 - len(deck[i]), end=' ')
    else:
        print('ERROR', end='')
    print()
