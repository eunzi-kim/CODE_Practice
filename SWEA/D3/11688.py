# Calkin-Wilf tree 1

T = int(input())
for TC in range(1, T+1):
    String = input()
    # 돌아가면서 이동 확인
    a = b = 1
    for x in String:
        if x == 'L':
            b += a
        else:
            a += b
    print("#{} {} {}".format(TC, a, b))