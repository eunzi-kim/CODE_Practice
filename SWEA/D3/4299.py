# 태혁이의 사랑은 타이밍

T = int(input())
for TC in range(1, T+1):
    D, H, M = map(int, input().split())
    result = 0
    # 너무 불쌍한 경우
    if D < 11 or (D <= 11 and H < 11) or (D <= 11 and H <= 11 and M < 11):
        result = -1
    # 약속 시간부터 차인 경우
    else:
        # 분
        if 11 <= M:
            result += M - 11
            if 11 <= H:
                result += (H - 11) * 60
            else:
                result += (13 + H) * 60
                D -= 1
        else:
            result += 60 + M - 11
            H -= 1
            if 11 <= H:
                result += (H - 11) * 60
            else:
                result += (13 + H) * 60
                D -= 1
        result += (D - 11) * 24 * 60
    print("#{} {}".format(TC, result))