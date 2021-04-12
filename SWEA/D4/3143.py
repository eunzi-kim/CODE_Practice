T = int(input())
for TC in range(1, T+1):
    A, B = input().split()
    # 중복 문자열 개수 초기화
    count = 0
    i = 0
    while i <= len(A) - len(B):
        # 첫 글자가 같은 경우
        if A[i] == B[0]:
            # 동일 문자열 탐색
            for j in range(i, i+len(B)):
                # 동일 문자열 아닐 경우 정지
                if A[j] != B[j-i]:
                    break
            # 동일 문자열 카운트
            else:
                count += 1
                i += len(B) - 1
        i += 1
    result = len(A) - count * len(B) + count
    print("#{} {}".format(TC, result))