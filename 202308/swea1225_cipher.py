for t in range(1,11):
    input()
    cipher = list(map(int, input().split()))
    while cipher[-1] > 0:
        for i in range(1,6):
            cipher[0] -= i
            num = cipher.pop(0)
            if num < 0:
                num = 0
            cipher.append(num)
            if num == 0:
                break

    print(f'#{t}', *cipher)
