def solution(s):
    answer = True
    Stack = []
    for x in s:
        # '("이면 Stack에 추가!
        if x == "(":
            Stack.append(x)
        # ")"
        elif x == ")":
            # Stack에 아무것도 없으면 실패
            if len(Stack) == 0:
                answer = False
                break
            # Stack에 "("이 있으면 1개 삭제
            else:
                Stack.pop(-1)
    # Stack에 남은 "("이 있으면 실패
    if len(Stack) != 0:
        answer = False
    return answer