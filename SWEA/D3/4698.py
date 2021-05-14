# 테네스의 특별한 소수

# 소수
Prime = []
# 1과 자신을 제외한 약수 존재 체크
Check = [0] * (10**6+1)
for i in range(2, 10**6+1):
    # 1과 자신을 제외하고 약수가 존재하지 않음 => 소수
    if Check[i] == 0:
        Prime.append(i)
        # 자신의 배수들 체크
        for j in range(i, 10**6+1, i):
            Check[j] = 1

T = int(input())
for TC in range(1, T+1):
    D, A, B = map(int, input().split())
    # 특별한 소수 개수
    result = 0
    # 소수들 중에서 특별한 소수 탐색!
    for x in Prime:
        if A <= x <= B and str(D) in str(x):
            result += 1
        # 탐색 범위 넘어가면, 반목문 탈출
        if x > B:
            break
    print("#{} {}".format(TC, result))