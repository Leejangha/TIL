def solution(spell, dic):
    answer = 2

    arr = []
    # spell의 원소가 dic의 원소안에 있을경우 arr에 추가
    for word in dic:
        for char in spell:
            if char in word:
                arr.append(word)
        # arr에서 dic의 원소별 개수를 계산하여 spell의 개수와 같으면 1출력
        if arr.count(word) == len(spell):
            answer =1

    return answer