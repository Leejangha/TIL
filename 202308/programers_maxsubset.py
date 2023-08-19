def solution(n, s):
    answer = []
    subsets = []
    max_mul = 0
    results = []
    
    A = list(range(s))
    for i in range(1<<s):
        arr = []
        for j in range(1, s):
            if i & (1<<j):
                arr.append(A[j])
            if len(arr) == n:
                subsets.append(arr)
    for subset in subsets:
        if sum(subset) == s:
            answer.append(subset)
    
    print(answer)
    for n in range(len(answer)):
        result = 1
        for num in answer[n]:
            result *= num
        if result > max_mul:
            max_mul = result
            results = num

    return results

solution(2, 9)