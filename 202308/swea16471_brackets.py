T = int(input())

brackets = ['(', ')', '{', '}', '[', ']']


def push(item):
    s.append(item)


for t in range(1, T+1):
    string = input()

    s = []
    for char in string:
        if char in brackets:
            if len(s) != 0:
                if char == ')' and s[-1] == '(':
                    s.pop()
                elif char == '}' and s[-1] == '{':
                    s.pop()
                elif char == ']' and s[-1] == '[':
                    s.pop()
                else:
                    s.append(char)
            else:
                s.append(char)

    if len(s) == 0:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
