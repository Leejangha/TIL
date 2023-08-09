T = int(input())


def push(item):
    s.append(item)


for t in range(1, T+1):
    string = input()

    s = []
    for char in string:
        if len(s) != 0:
            if char == s[-1]:
                s.pop()
            elif char == s[-1]:
                s.pop()
            elif char == s[-1]:
                s.pop()
            else:
                s.append(char)
        else:
            s.append(char)

    res = len(s)

    print(f'#{t} {res}')
