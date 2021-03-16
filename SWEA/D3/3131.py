# 100만 이하의 모든 소수

N = [1] * 1000001
# 0과 1은 소수가 아님
N[0] = N[1] = 0
# 소수의 배수들은 소수가 아님
for i in range(2, len(N)):
    if N[i] == 1:
        # i가 소수일 때, i의 배수들을 모두 처리하자
        # j = 2*i, 3*i, ...
        for j in range(i ** 2, len(N), i):
            N[j] = 0
# 소수탐색
for i in range(len(N)):
    if N[i]:
        print(i, end=" ")