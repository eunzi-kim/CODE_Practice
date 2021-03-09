# 홀수일까 짝수일까

T = int(input())
for TC in range(1, T+1):
    number = int(input())
    # 홀수
    if number % 2:
        result = "Odd"
    # 짝수
    else:
        result = "Even"
    print("#{} {}".format(TC, result))