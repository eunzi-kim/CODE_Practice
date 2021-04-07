# 승률 비교하기

T = int(input())
Result = []
for _ in range(T):
    A, B, C, D = map(int, input().split())
    if A / B > C / D:
        result = 'ALICE'
    elif A / B < C / D:
        result = 'BOB'
    else:
        result = 'DRAW'
    Result.append(result)
for tc in range(T):
    print("#{} {}".format(tc+1, Result[tc]))