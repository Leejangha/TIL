# 입력값 받기
N = int(input())
store = list(map(int, input().split()))
M = int(input())
customer = list(map(int, input().split()))

# store 정렬
store.sort()

# 손님의 부품 각각을 가게의 목록 에서 이진 탐색을 실행
for c in customer:
    start = 0
    end = N
    res = 'no'
    # 시작 값이 끝값과 크거나 같아질 때 까지 탐색 반복
    while start <= end:
        mid = int((start + end) / 2)
        if store[mid] > c:
            end = mid-1
        elif store[mid] < c:
            start = mid+1
        else:
            res = 'yes'
            break
    print(res, end=' ')
