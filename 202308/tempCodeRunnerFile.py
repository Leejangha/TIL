def solution(a, b, g, s, w, t):
    answer = -1
    max_time = max(t)
    total_weight = 0
    g_weight = 0
    s_weight = 0
    
    for i in len(t):
        total_weight += (max_time // t[i]) * w[i]

    n = 0
    if (a+b) % total_weight != 0:
        n = (a+b) // total_weight + 1
    else:
        n = (a+b) // total_weight
    
    for i in len(t):
        g_weight += (max_time // t[i]) * g[i] * n
        s_weight += (max_time // t[i]) * s[i] * n

    if a <= g_weight and b <= s_weight:
        answer = max_time * n
    else:
        answer = max_time * n * max(a//g_weight+1, b//s_weight+1)

    return answer