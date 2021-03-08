# 민석이의 과제 체크하기

T = int(input())
for TC in range(1, T+1):
    N, K = map(int, input().split())
    Good = list(map(int, input().split()))
    All = [x for x in range(1, N+1)]
    while Good:
        v = Good.pop(-1)
        for i in range(len(All)):
            if All[i] == v:
                All.pop(i)
                break
    result = ""
    for a in All:
        result += str(a) + " "
    print("#{} {}".format(TC, result))