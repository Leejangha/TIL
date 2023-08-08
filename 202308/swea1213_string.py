for t in range(1, 11):
    input()
    string = input()
    N = len(string)
    sentence = input()
    M = len(sentence)
    res = 0

    for i in range(M):
        if sentence[i:i+N] == string:
            res += 1

    print(f'#{t} {res}')


# count 사용
for t in range(1, 11):
    input()
    string = input()
    sentence = input()
    res = sentence.count(string)

    print(f'#{t} {res}')
