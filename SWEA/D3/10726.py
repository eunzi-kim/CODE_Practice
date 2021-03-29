# 이진수 표현

# 이진수는 2로 계속 나누면서
# 나머지들을 자리수를 올려가며 넣어주며 나타낼 수 있음.
# => 이를 이용하여 나누면서 확인!
T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    # N번 반복
    for _ in range(N):
        # 비트가 1이 켜지지 않은 경우,
        # 'OFF' 출력 후 끝!
        if M % 2 != 1:
            result = 'OFF'
            break
        else:
            M //= 2
            result = 'ON'
    print("#{} {}".format(TC, result))