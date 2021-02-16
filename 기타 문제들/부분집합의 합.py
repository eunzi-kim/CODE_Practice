# 0216 복습
# SWEA 4837

T = int(input())
for TC in range(1, T+1):
    N, K = map(int, input().split())

    A = [n for n in range(1, 13)]

    # 모든 부분집합 리스트
    S = []
    for i in range(1 << 12):
        # 부분집합 리스트
        subS = []
        for j in range(12):
            if i & (1 << j):
                subS.append(A[j])
        S.append(subS)

    # 부분집합들 중 조건에 맞는 값 탐색하여 카운트
    # 카운트 초기화
    count = 0
    for s in S:
        sumV = 0
        for x in s:
            sumV += x
        if len(s) == N and sumV == K:
            count += 1
    print(f'#{TC} {count}')