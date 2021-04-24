from collections import deque

T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    Queue = deque()
    chk = [0] * 1000001
    chk[N] = 1
    Queue.append((N, 0))
    while Queue:
        w = Queue.popleft()
        v = w[0]
        count = w[1]
        if v == M:
            result = count
            break
        V = [v*2, v+1, v-1, v-10]
        for x in V:
            if 0 < x <= 1000000 and chk[x] == 0:
                chk[x] = 1
                Queue.append((x, count+1))
    print("#{} {}".format(TC, result))