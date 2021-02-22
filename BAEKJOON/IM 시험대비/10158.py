# 개미

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# 격자 공간 초기화
Space = [[0 for _ in range(w+1)] for _ in range(h+1)]

# 이동 변수 리스트
d = [1, -1]

# 시간 초기화
time = 0
i = j = 0
dp = dq = 1
while time < t:
    # 격자 공간 초기화
    Space = S
    # 막히는 벽이 없을 경우의 개미 이동
    if 0 <= q+dq <= h and 0 <= p+dp <= w:
        q += dq
        p += dp
        Space[q][p] = 1
        time += 1
    # 좌우로 벽이 있는 경우
    elif 0 <= q+dq <= h:
        if dp == 1:
            dp = -1
        else:
            dp = 1
    # 상하로 벽이 있는 경우
    elif 0 <= p+dp <= w:
        if dq == 1:
            dq = -1
        else:
            dq = 1

print(p, q)

##################################################

# 시간 초기화
dp = dq = 1
for time in range(t):
    # 막히는 벽이 없을 경우의 개미 이동
    if 0 <= q+dq <= h and 0 <= p+dp <= w:
        dq = dq
        dp = dp
    # 좌우로 벽이 있는 경우
    elif 0 <= q+dq <= h:
        if dp == 1:
            dp = -1
        else:
            dp = 1
    # 상하로 벽이 있는 경우
    else:
        if dq == 1:
            dq = -1
        else:
            dq = 1
    q += dq
    p += dp

print(p, q)