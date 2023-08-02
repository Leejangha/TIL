# 조합
def combination(numbers):
    combinations = []
    for i in range(len(numbers)-2):
        for j in range(i+1, len(numbers)-1):
            for k in range(j+1, len(numbers)):
                sum = 0
                sum = numbers[i] + numbers[j] + numbers[k]
                combinations.append(sum)
    return combinations

A = list(range(1, 13))
print(A)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

N =6
com = int(factorial(12)/factorial(N)/factorial(12-N))

print(com)