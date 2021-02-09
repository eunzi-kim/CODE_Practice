# 0209 수업 복습
# 전기버스

# K : 최대한 이동할 수 있는 정류장 수
# N : 정류장 종점
# M : 충전기 수

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    Chg = list(map(int, input().split()))

    # 인덱스 이용하기 위한 리스트!
    # 충전기 있는 곳 : 1, 없는 곳 : 0
    C = [0] * (N+1)
    for x in Chg:
        C[x] += 1
    
    i = K
    count = 0
    j = 0
    while i < N:
        # 충전기 이용하는 상황
        if C[i] == 1:
            count += 1 
            j = i
            i += K

        # 충전기 없는 상황 
        # => 충전기 있는 곳으로 가기
        else:
            i -= 1
            # 충전기 설치가 잘못된 경우
            if i == j:
                count = 0
                break
        
    print(f'#{tc} {count}')

