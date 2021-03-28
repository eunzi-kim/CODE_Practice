# 몬스터 사냥

T = int(input())
for TC in range(1, T+1):
    D, L, N = map(int, input().split())
    # 가한 총 데미지 초기화
    damage = 0
    # N번의 공격동안 가한 총 데미지 더하기
    for n in range(N):
        damage += D * (1 + n * 0.01 * L)
    print("#{} {}".format(TC, int(damage)))