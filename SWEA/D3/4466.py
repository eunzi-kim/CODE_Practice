# 최대 성적표 만들기

T = int(input())
for TC in range(1, T+1):
    N, K = map(int, input().split())
    Score = list(map(int, input().split()))
    Score.sort()
    sum = 0
    for i in range(N-1, N-1-K, -1):
        sum += Score[i]
    print("#{} {}".format(TC, sum))