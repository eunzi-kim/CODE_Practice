# 방 배정
N, K = map(int, input().split())
Sex = [0] * N # 여학생: 0, 남학생: 1
Year = [0] * N
for n in range(N):
    S, Y = map(int, input().split())
    Sex[n] = S
    Year[n] = Y

# 성별, 학년별 학생수 리스트
# 리스트 초기화
G = [[0] * 6 for _ in range(2)]
# 행은 성별, 열은 학년별
for i in range(N):
    if Sex[i] == 0:
        G[0][Year[i] - 1] += 1
    elif Sex[i] == 1:
        G[1][Year[i] - 1] += 1

# 성별, 학년별 학생들의 방 나누기
count = 0
for i in range(2):
    for j in range(6):
        # 학생수 + (K - 1)을 K로 나눈 몫으로 학생들 방의 개수를 구한다.
        count += (G[i][j] + (K-1)) // K

print(count)