for t in range(int(input())):
    Bin = input()
    Tri = input()
    for i in range(len(Bin)):
        if Bin[i] == '1':
            Bin_i = Bin[:i] + '0' + Bin[i+1:]
        else:
            Bin_i = Bin[:i] + '1' + Bin[i+1:]
        for j in range(len(Tri)):
            for k in range(3):
                if Tri[j] != str(k):
                    Tri_j = Tri[:j] + str(k) + Tri[j+1:]
                if int(Tri_j, 3) == int(Bin_i, 2):
                    res = int(Tri_j, 3)
    print(f'#{t+1} {res}')
