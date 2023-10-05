hex_nums = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


for t in range(int(input())):
    N = int(input())
    hex_num = input()
    P = int(input(), 16)
    ans = ""
    for char in hex_num:
        num = int(char, 16) ^ P
        if num in hex_nums:
            ans += hex_nums[num]
        else:
            ans += str(num)
    print(f'#{t+1} {ans}')
