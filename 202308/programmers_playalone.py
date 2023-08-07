def solution(cards):
    box1 = []
    answer = []
    max_mul = 0

    for i in range(len(cards)):
        if cards[i] not in box1:
            box2 = []
            j = 0

            box2.append(cards[i])
            while cards[box2[j] - 1] not in box2:
                box2.append(cards[box2[j] - 1])
                box1.append(cards[box2[j] - 1])
                j += 1
            answer.append(len(box2))

    answer.sort()
    max_mul = answer[-1] * answer[-2]

    return max_mul


def solution(cards):
    box2 = []
    answer = []
    max_mul = 0
    j = 0

    for i in range(len(cards)):

        if cards[i] not in box2:

            cnt = 1

            box2.append(cards[i])
            while cards[box2[j] - 1] not in box2:
                box2.append(cards[box2[j] - 1])

                j += 1
                cnt += 1
            answer.append(cnt)
            j += 1


    answer.sort()
    max_mul = answer[-1] * answer[-2]

    return max_mul

cards = list(map(int, input().split()))
print(solution(cards))