# 항구에 들어오는 배

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    Ship = [int(input()) for _ in range(N)]
    # 배 체크리스트 초기화
    Check = [1]
    i = 1
    result = 0
    while Ship != sorted(Check):
        v = Ship[i]
        if v not in Check:
            Check.append(v)
            result += 1
            cycle = v - 1
            for j in range(i+1, len(Ship)):
                if Ship[j] - v == cycle:
                    v = Ship[j]
                    if Ship[j] not in Check:
                        Check.append(Ship[j])
        i += 1
    print("#{} {}".format(TC, result))