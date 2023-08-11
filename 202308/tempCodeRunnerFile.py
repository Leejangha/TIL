def solution(a, b, g, s, w, t):
    answer = 0
    g_per = []
    s_per = []

    for i in range(len(t)):
        g_per.append((g[i]*t[i])/w[i])
        s_per.append((s[i]*t[i])/w[i])
    
    g_idx = g_per.index(max(g_per))
    s_idx = s_per.index(max(s_per))
    
    if max(g_per) > max(s_per) :
                    max_t = max(g_per)
                    idx = g_idx
    else:
        max_t = max(s_per)
        idx = s_idx
    answer = (max_t -1)//t[idx]+1

    return answer*2 -1


print(solution(10, 10, [100], [100], [7], [10]))
print(solution(90, 500, [70,70,0], [0,0,500], [100,100,2], [4,8,1]))
 