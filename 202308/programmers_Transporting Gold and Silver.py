# def solution(a, b, g, s, w, t):
#     answer = 0
#     weight_per = []
#     g_per = []
#     s_per = []
#     g_w_per = 0
#     s_w_per = 0
#     times = max(t)

#     for i in range(len(t)):
#         weight_per.append(w[i]/t[i])
#         g_per.append((g[i]-1)//weight_per[i]+1)
#         s_per.append((s[i]-1)//weight_per[i]+1)

#     for i in range(len(t)):
#         if g_per[i] != 0:
#             g_w_per += weight_per[i]
#         if s_per[i] != 0:
#             s_w_per += weight_per[i]

#     atleast = (a+b-1)//sum(w)+1
#     for i in range(len(t)):
#         if ((a-1)//(g_w_per*t[i])+1) > atleast:
#             atleast = (a-1)//(g_w_per*t[i])+1
#             times = t[i]
#         if ((b-1)//(s_w_per*t[i])+1) > atleast:
#             atleast = (b-1)//(s_w_per*t[i])+1
#             times = t[i]

#     answer = int((atleast*2 -1)*times)

#     return answer

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
    print(max_t)
    answer = (max_t -1)//t[idx]+1

    return answer*2 -1


print(solution(10, 10, [100], [100], [7], [10]))
print(solution(90, 500, [70,70,0], [0,0,500], [100,100,2], [4,8,1]))
 