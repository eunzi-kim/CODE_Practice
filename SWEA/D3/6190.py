# 정곤이의 단조 증가하는 수
T = int(input())
for TC in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    # 결과값 초기화
    result = 0
    # 모든 경우의 수 곱하기
    for i in range(N-1):
        for j in range(i+1, N):
            val = str(A[i] * A[j])
            # 단조 증가 카운트
            cnt = 1
            for k in range(len(val)-1):
                # 단조 증가하지 않으면 break
                if int(val[k]) > int(val[k+1]):
                    cnt = 0
                    break
                # 단조 증가하면 카운트
                else:
                    cnt += 1
            # 단조 증가하는 수일 때 최대값 탐색
            if cnt == len(val) and result < int(val):
                result = int(val)
    # 단조 증가하는 수가 없는 경우
    if result == 0:
        result = -1
    print("#{} {}".format(TC, result))
