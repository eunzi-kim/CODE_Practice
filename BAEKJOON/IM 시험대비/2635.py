# 수 이어가기

T = int(input())

maxC = 0
for x in range(T, -1, -1):

    a = T
    b = c = x
    count = 1
    while c >= 0:
        c = a - b
        a = b
        b = c
        count += 1

    if count > maxC:
        maxC = count
        maxX = x

t = T
p = q = maxX
result = str(T)
for i in range(maxC-1):
    q = t - p
    t = p
    p = q
    result += " " + str(t)

print("{}\n{}".format(maxC, result))