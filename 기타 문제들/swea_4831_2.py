# 0209 수업 복습
# 전기버스 다른 방법!

# K : 최대한 이동할 수 있는 정류장 수
# N : 정류장 종점
# M : 충전기 수

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    C = list(map(int, input().split()))

    C.insert(0, 0)
    C.append(N)

    x = 0
    count = 0
    for i in range(1, M+2):
        if C[i] - C[i-1] > K:
            count = 0
            break

        if C[i] > K + x:
            count += 1
            x = C[i-1]

    print(f'#{tc} {count}')