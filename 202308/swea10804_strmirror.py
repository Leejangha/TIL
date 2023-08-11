T = int(input())
lst = ['', 'b', 'p', 'q', 'd']

for t in range(1, T+1):
    string = input()
    res = ''
    for char in string:
        res += lst[lst.index(char) * (-1)]
    print(f'#{t} {res[::-1]}')
