# 반반

T = int(input())
for TC in range(1, T+1):
    Arr = input()
    # 결과값 초기화
    result = 'Yes'
    # 알파벳 개수 리스트
    S = [0] * 26
    for a in Arr:
        # 알파벳 인덱스
        i = ord(a) - 65
        S[i] += 1
        # 만약 알파벳이 2개 넘기는 경우
        if S[i] > 2:
            result = 'No'
            break
    # 만약 알파벳 종류가 2가지 이상인 경우
    count = 0
    for s in S:
        if s != 0:
            count += 1
        if count > 2:
            result = "No"
            break
    print("#{} {}".format(TC, result))