# 2016년 요일 맞추기

T = int(input())
for TC in range(1, T+1):
    M, D = map(int, input().split())
    d = 0
    # 월 => 일 단위로 변경
    for x in range(1, M):
        if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10:
            d += 31
        elif x == 2:
            d += 29
        else:
            d += 30
    # 일 수의 차이 더해주기
    d += D - 1
    # 요일 탐색
    # d == 0일 때, 요일이 4이므로
    # 4를 더해주고 mod7을 이용한다.
    result = (d + 4) % 7
    print("#{} {}".format(TC, result))