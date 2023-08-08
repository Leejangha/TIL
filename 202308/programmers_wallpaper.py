def solution(wallpaper):
    lux, luy, rdx, rdy = 0, 50, 0, 0
    row = []
    cnt = 0
    for x in wallpaper:
        if '#' in x:
            row.append(cnt)
        cnt += 1
    lux = min(row)
    rdx = max(row) + 1

    for y in wallpaper:
        idx = 0
        for char in y:
            if char == '#':
                if luy > idx:
                    luy = idx
                if rdy < idx + 1:
                    rdy = idx + 1
            idx += 1

    return [lux, luy, rdx, rdy]

# 수정
def solution(wallpaper):
    x = []
    y = []

    # 바탕화면에서 '#'의 위치 인덱스를 x, y에 저장
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)
    # 시작점은 x, y의 최솟값, 끝점은 x, y의 최댓값 +1
    lux, luy = min(x), min(y)
    rdx, rdy = max(x)+1, max(y)+1

    return [lux, luy, rdx, rdy]
