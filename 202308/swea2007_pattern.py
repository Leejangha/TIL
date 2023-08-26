for t in range(int(input())):
    STR = input()
    for i in range(2,11):
        if STR[:i] == STR[i:i*2]:
            res = i
            break

    print(f'#{t+1} {res}')
