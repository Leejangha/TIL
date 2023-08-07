T = int(input())

for t in range(1, T+1):
    N = int(input())

    # 테이블 입력
    table = list(map(int, input().split()))

    # 획득 점수 총합
    total_sum = 0

    # N번의 챌린지 실행
    for i in range(1, N+1):
        # N번째 챌린지의 점수
        N_sum = 0
        # 0부터 i거리 만큼 튕기면서 점수 더하기
        for j in range(0, N, i):
            N_sum += table[j]
        # 전체 점수에 N번째 챌린지의 점수를 더함
        total_sum += N_sum

    # 전체 점수가 0점 이하인 경우 0점으로 출력
    if total_sum < 0:
        total_sum = 0

    print(f'#{t} {total_sum}')
