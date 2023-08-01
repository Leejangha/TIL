def min_score(scores):
    # pass
    # 여기에 코드를 작성합니다.
    min = 100
    for score in scores:
        if min > score:
            min = score
    return min


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    print(min_score(scores)) # 30
    # 아래 부터 추가 예제 코드 작성 가능합니다.
    
