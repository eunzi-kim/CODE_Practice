# 제곱 팰린드롬 수

# 팰린드롬 수 체크 함수
def check(A):
    # 한자리수는 무조건 팰린드롬 수!
    if len(A) == 1:
        return 1
    # 가운데부터 팰린드롬 수 체크!
    else:
        i = len(A) // 2 - 1
        # 홀수 인덱스
        if len(A) % 2:
            j = i + 2
        # 짝수 인덱스
        else:
            j = i + 1
        while j < len(A):
            if A[i] == A[j]:
                i -= 1
                j += 1
            else:
                return 0
            if j == len(A):
                return 1
            return 0

T = int(input())
for TC in range(1, T+1):
    A, B = map(int, input().split())
    count = 0
    for x in range(A, B+1):
        number = list(str(x))
        # 제곱근이 실수가 아닌 경우, 팰린드롬 수가 될 수 없다.
        if x ** 0.5 != int(x ** 0.5):
            continue
        else:
            number2 = list(str(int(x ** 0.5)))
        if check(number) == 1 and check(number2) == 1:
            count += 1
    print("#{} {}".format(TC, count))