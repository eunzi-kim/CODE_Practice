# 세상의 모든 팰린드롬

T = int(input())
for TC in range(1, T+1):
    String = list(input())
    # 문자열의 길이가 1인 경우
    if len(String) == 1:
        result = 'Exist'
    while len(String) > 1:
        # 문자열의 맨 앞글자와 끝 글자를 빼서 비교하기
        v1 = String.pop(0)
        v2 = String.pop(-1)
        # 문자열의 맨 앞글자와 끝 글자가 다른 경우, 존재하지 않음
        if v1 != v2 and v1 != '?' and v2 != '?':
            result = 'Not exist'
            break
        # 가운데까지 모든 양 옆 글자들이 같은 경우, 존재
        if len(String) <= 1:
            result = 'Exist'
    print("#{} {}".format(TC, result))