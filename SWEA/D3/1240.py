# 단순 2진 암호코드
info = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    Arr = [list(input()) for _ in range(N)]
    # 코드 추출
    Code = ''
    for r in range(N):
        code = 0
        for c in range(M-1, -1, -1):
            if Arr[r][c] == '1':
                code = c
                break
        if code and len(Code) == 0:
            for c in range(code-55, code+1):
                Code += Arr[r][c]
    # 코드 확인
    N = []
    for i in range(0, 56, 7):
        number = ''
        for j in range(i, i+7):
            number += Code[j]
        for j in range(10):
            if number == info[j]:
              N.append(j)
    # 결과값 초기화
    result = 0
    # 코드 검증
    if ((N[0] + N[2] + N[4] + N[6]) * 3 + N[1] + N[3] + N[5] + N[7]) % 10 == 0:
        for k in range(8):
            result += N[k]
    print("#{} {}".format(TC, result))