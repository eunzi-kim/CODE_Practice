# 더하기 사이클
# 26 68 84 42 26 => 4
# 55 50 05 55 => 3

T = int(input())

count = 0
t = T
while t != T or count == 0:
    count += 1
    if t >= 10:
        r = t % 10
        q = t // 10
        n = r + q
        if n >= 10:
            n -= 10
    
    else:
        r = t % 10
        n = r

    t = 10 * r + n
    
    
print(count)