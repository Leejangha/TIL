T = int(input())

for t in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    def binary_search(page):
        l = P
        r = 1
        count = 0
        c = int((l+r) / 2)
        while c != page:
            c = int((l+r) / 2)
            if page > c:
                count += 1
                r = c
            else:
                count += 1
                l = c
        return count

    if binary_search(Pa) < binary_search(Pb):
        result = 'A'
    elif binary_search(Pa) > binary_search(Pb):
        result = 'B'
    else:
        result = 0

    print(f'#{t} {result}')