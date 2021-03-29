# 세상의 모든 팰린드롬 2

T = int(input())
for TC in range(1, T+1):
    String = list(input())
    result = 'Exist'
    while len(String) > 1:
        v1 = String[0]
        v2 = String[-1]
        # 팰린드롬이 아닌 경우
        if v1 != v2 and v1 != '*' and v2 != '*':
            result = 'Not exist'
            break
        # 와일드키가 있으면 무조건 팰린드롬!
        elif v1 == '*' or v2 == '*':
            result = 'Exist'
            break
        # 양 사이드에서 하나씩 비교하므로 빼주기
        else:
            String.pop(0)
            String.pop(-1)
    print("#{} {}".format(TC, result))