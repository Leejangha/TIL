def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

N =6
com = int(factorial(12)/factorial(N)/factorial(12-N))

print(com)