T = int(input())


def push(item, stack):
    stack.append(item)


for t in range(1, T+1):
    pipe = input()
    stack = []
    cnt = 0
    is_pipe = True

    for char in pipe:
        if stack:
            if char == '(': 
                is_pipe = True
                push(char, stack)
            else:
                if is_pipe:
                    stack.pop()
                    cnt += len(stack)
                    is_pipe = False
                else:
                    stack.pop()
                    cnt += 1
        else:
            push(char, stack)

    print(f'#{t} {cnt}')
