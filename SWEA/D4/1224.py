# 계산기3

for TC in range(1, 11):
    N = int(input())
    String = list(input())
    # 후위식 표기
    Stack = []
    Stack2 = []
    for x in String:
        # 연산자 => Stack2
        if x == '+':
            if Stack2[-1] == '*' or Stack2[-1] == '+':
                v = Stack2.pop(-1)
                Stack.append(v)
                if Stack2[-1] == "+":
                    w = Stack2.pop(-1)
                    Stack.append(w)
                Stack2.append(x)
            else:
                Stack2.append(x)
        elif x == '*':
            if Stack2[-1] == '*':
                v = Stack2.pop(-1)
                Stack.append(v)
            Stack2.append(x)
        elif x == '(':
            Stack2.append(x)
        elif x == ')':
            while Stack2[-1] != '(':
                v = Stack2.pop(-1)
                if v != '(':
                    Stack.append(v)
            if Stack2[-1] == '(':
                v = Stack2.pop(-1)
        # 숫자 => Stack
        else:
            Stack.append(x)
    # 계산하기
    Stack1 = []
    for x in Stack:
        # 연산자
        if x == '*':
            v2 = Stack1.pop(-1)
            v1 = Stack1.pop(-1)
            Stack1.append(int(v1) * int(v2))
        elif x == '+':
            v2 = Stack1.pop(-1)
            v1 = Stack1.pop(-1)
            Stack1.append(int(v1) + int(v2))
        # 숫자
        else:
            Stack1.append(x)
    print("#{} {}".format(TC, Stack1[0]))