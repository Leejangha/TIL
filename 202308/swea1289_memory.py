for t in range(int(input())):
    mem = input()
    if mem[0] == '0':
        res = 0
    else:
        res = 1
    for i in range(len(mem)-1):
        if mem[i] != mem[i+1]:
            res += 1

    print(f'#{t+1} {res}')
