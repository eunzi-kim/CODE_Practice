# 중위순회
def search(x):
    global result
    # x의 왼쪽 자식 존재 => 탐색
    if len(Child[x]):
        search(Child[x][0])
    # 자신 위치에서 추가
    result += String[x][0]
    # x의 오른쪽 자식 존재 => 탐색
    if len(Child[x]) == 2:
        search(Child[x][1])

for TC in range(1, 11):
    T = int(input())
    # 자식 리스트
    Child = [[] for _ in range(T+1)]
    # 문자 리스트
    String = [[] for _ in range(T+1)]
    for _ in range(T):
        Input = list(input().split())
        # 문자 리스트 완성
        String[int(Input[0])].append(Input[1])
        # 자식 리스트 완성
        if len(Input) >= 3:
            Child[int(Input[0])].append(int(Input[2]))
        if len(Input) == 4:
            Child[int(Input[0])].append(int(Input[3]))
    # 결과 초기화
    result = ''
    search(1)
    print("#{} {}".format(TC, result))