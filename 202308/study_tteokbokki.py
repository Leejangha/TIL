# 입력값 받기
N, M = map(int, input().split())
H = list(map(int, input().split()))

# H 정렬
H.sort()

# 손님의 부품 각각을 가게의 목록 에서 이진 탐색을 실행
start = 0
end = H[-1]
res = []
# 시작 값이 끝값과 크거나 같아질 때 까지 탐색 반복
while start <= end:
    mid = int((start + end) / 2)
    m = 0
    for h in H:
        if h - mid > 0:
            m += h - mid
    if m < M:
        end = mid-1
    elif m >= M:
        res.append(mid)
        start = mid+1

print(max(res))
