# 영준이의 카드 카운팅

T = int(input())
for TC in range(1, T+1):
    S = list(input())
    # S, D, H, C
    # 카드 정보 담기
    Card = [[] for _ in range(4)]
    for i in range(0, len(S), 3):
        if S[i] == 'S':
            Card[0].append(S[i+1] + S[i+2])
        elif S[i] == 'D':
            Card[1].append(S[i+1] + S[i+2])
        elif S[i] == 'H':
            Card[2].append(S[i+1] + S[i+2])
        else:
            Card[3].append(S[i+1] + S[i+2])
    result = ''
    for i in range(4):
        # 카드 숫자가 다를 경우, 스택에 넣기
        Stack = []
        for j in range(len(Card[i])):
            if Card[i][j] not in Stack:
                Stack.append(Card[i][j])
            # 동일한 카드인 경우, 'ERROR' 발생!
            else:
                result = 'ERROR'
        # ERROR가 아닌 경우, 부족한 카드의 개수 탐색
        if result != 'ERROR':
            result += str(13-len(Stack)) + " "
    print("#{} {}".format(TC, result))