def solution(a, b, g, s, w, t):
    answer = -1
    max_time = max(t)
    total_weight = 0
    g_weight = 0
    s_weight = 0

    for i in range(len(t)):
        total_weight += (max_time // t[i]) * w[i]

    n = 0
    if (a+b) % total_weight != 0:
        n = (a+b) // total_weight + 1
    else:
        n = (a+b) // total_weight
    
    for i in range(len(t)):
        g_weight += (max_time // t[i]) * min(g[i],w[i]) * n
        s_weight += (max_time // t[i]) * min(s[i],w[i]) * n

    if a <= g_weight and b <= s_weight:
        answer = max_time * (2*n-1)
    else:
        answer = max_time * (2*n-1) * max(a//g_weight+1, b//s_weight+1)

    return answer