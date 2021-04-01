# 무한 사전

T = int(input())
for TC in range(1, T+1):
    P = input().rstrip()
    Q = input().rstrip()
    if P + 'a' != Q:
        result = 'Y'
    else:
        result = 'N'
    print("#{} {}".format(TC, result))
