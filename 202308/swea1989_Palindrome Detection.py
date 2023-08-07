T = int(input())

for t in range(1, T+1):
    string = input()
    N = len(string)

    is_palin = 0
    for i in range(N//2):
        if string[i] == string[-1-i]:
            is_palin = 1
        else:
            is_palin = 0

    print(f'#{t} {is_palin}')
