def Run(p):
    for char in p:
        if (char+1) in p and (char+2) in p:
            return True


def Triplet(p):
    for char in p:
        if p.count(char) == 3:
            return True


for t in range(int(input())):
    deck = list(map(int, input().split()))
    p1 = []
    p2 = []
    res = 0
    while deck:
        p1.append(deck.pop(0))
        if len(p1) >= 3:
            if Run(p1) or Triplet(p1):
                res = 1
                break
        p2.append(deck.pop(0))
        if len(p2) >= 3:
            if Run(p2) or Triplet(p2):
                res = 2
                break

    print(f'#{t+1} {res}')
