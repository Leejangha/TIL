def solution(wallpaper):
    lux, luy, rdx, rdy = 0, 0, 0, 0
    wallpaper = list(wallpaper)
    row = []
    for x in wallpaper:
        if '#' in x:
            row.append(wallpaper.index(x))
    lux = min(row)
    rdx = max(row) + 1

    for y in wallpaper:
        if luy > y.index('#'):
            luy = y.index('#')
        if rdy < y.index('#') + 1:
            rdy = y.index('#') + 1

    return [lux, luy, rdx, rdy]

for _ in range(4):
    wallpaper = list(input().split(','))
    print(solution(wallpaper))