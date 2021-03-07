# 외로운 문자

T = int(input())
for TC in range(1, 1+T):
    String = list(input())
    Stack = []
    for i in range(len(String)):
        if String[i] not in Stack:
            Stack.append(String[i])
        else:
            for j in range(len(Stack)):
                if String[i] == Stack[j]:
                    Stack.pop(j)
                    break
    if len(Stack):
        result = "".join(sorted(Stack))
    else:
        result = "Good"
    print("#{} {}".format(TC, result))