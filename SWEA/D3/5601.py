# 쥬스 나누기

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    result = ""
    for n in range(N):
        result += "1/" + str(N) + " "
    print("#{} {}".format(TC, result))