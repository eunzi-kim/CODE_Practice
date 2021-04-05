import sys
sys.stdin = open('0405_input.txt', 'r')

for TC in range(1, 11):
    N = int(input())
    # 알파벳 리스트 초기화
    Word = [''] * (N+1)
    # 자식 리스트 초기화
    Child = [[] for _ in range(N+1)]
    for _ in range(N):
        Input = list(input().split())
        Word[int(Input[0])] = Input[1]
        if len(Input) >= 3:
            Child[int(Input[0])].append(Input[2])
        if len(Input) == 4:
            Child[int(Input[0])].append(Input[3])
    result = ''
    def check(root):
        global result
        # 왼쪽 자식
        if len(Child[root]) >= 1:
            check(root * 2)
        # 부모
        result += Word[root]
        # 오른쪽 자식
        if len(Child[root]) >= 2:
            check(root * 2 + 1)
    check(1)
    print("#{} {}".format(TC, result))