# USB 꽂기의 미스터리

T = int(input())
for TC in range(1, T+1):
    p, q = map(float, input().split())
    s1 = (1 - p) * q
    s2 = p * (1 - q) * q
    if s1 < s2:
        result = "YES"
    else:
        result = "NO"
    print("#{} {}".format(TC, result))
