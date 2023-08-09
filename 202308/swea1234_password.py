def push(item):
    password.append(item)


for t in range(1, 11):
    N, string = input().split()

    password = []
    for char in string:
        if len(password) != 0:
            if char == password[-1]:
                password.pop()
            else:
                push(char)
        else:
            push(char)

    print(f'#{t}', end=' ')
    print(''.join(password))
