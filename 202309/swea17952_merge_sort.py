def merge_sort(arr):
    global cnt
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    if low_arr[-1] > high_arr[-1]:
        cnt += 1

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


for t in range(int(input())):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    answer = merge_sort(numbers)
    print(f'#{t+1} {answer[N//2]} {cnt}')

# def merge_sort(arr):
#     def sort(low, high):
#         if high - low < 2:
#             return
#         mid = (low + high) // 2
#         sort(low, mid)
#         sort(mid, high)
#         merge(low, mid, high)
#
#     def merge(low, mid, high):
#         global cnt
#         temp = []
#         l, h = low, mid
#
#         while l < mid and h < high:
#             if arr[l] < arr[h]:
#                 temp.append(arr[l])
#                 l += 1
#             else:
#                 temp.append(arr[h])
#                 h += 1
#
#         while l < mid:
#             temp.append(arr[l])
#             l += 1
#
#         while h < high:
#             temp.append(arr[h])
#             h += 1
#
#         for i in range(low, high):
#             arr[i] = temp[i - low]
#
#     return sort(0, len(arr))
#
#
# for t in range(int(input())):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     cnt = 0
#     merge_sort(numbers)
#     print(f'#{t+1} {numbers[N//2]} {cnt}')
