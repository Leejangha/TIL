def solution(cards):
    answer = 0
    for i in range(len(cards)):
        box1 = []
        box2 = []
        result = []

        j = 0
        r = 0
        box1.append(cards[i])
        
        while cards[box1[j] - 1] in box1:
            box1.append(cards[box1[j] - 1])
            j += 1
        
        dif = list(set(cards).difference(box1))
        
        for k in dif:
            box2.append(cards[k - 1])
            
            while cards[box2[r] - 1] in box2:
                box2.append(cards[box2[r] - 1])
                r += 1
        
        result.append(j * r)
    
    answer = max(result)
    print(answer)
    return

cards = [8, 6, 3, 7, 2, 5, 1, 4]
solution(cards)