# 직사각형 길이 찾기

T = int(input())
for TC in range(1, T+1):
    L = list(map(int, input().split()))
    Stack = []
    for i in range(3):
        Stack.append(L[i])
        if len(Stack) >= 2 and Stack[0] == L[i]:
            Stack.pop(-1)
            Stack.pop(0)
    print("#{} {}".format(TC, Stack[0]))