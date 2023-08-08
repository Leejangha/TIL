def solution(n):
    answer = 0

    # n이하의 자연수
    for num in range(1, n+1):
        # 약수의 개수 계산
        divisor = 0
        for i in range(1, num+1):
            if num % i == 0:
                divisor += 1
        # 합성수 개수 계산
        if divisor >= 3:
            answer += 1

    return answer