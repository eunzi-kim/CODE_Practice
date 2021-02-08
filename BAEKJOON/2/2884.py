# 알람 시계

h, m = map(int, input().split())

if m - 45 < 0:
    m = m + 60 - 45

    if h > 0:
        h -= 1
    else:
        h = h + 24 -1
        
else:
    m = m - 45

    if h < 0:
        h = h + 24

print(h, m)