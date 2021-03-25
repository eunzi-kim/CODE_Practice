# 새샘이의 7-3-5 게임

T = int(input())
for TC in range(1, T+1):
    Number = list(map(int, input().split()))
    Number.sort()
    Sub = []
    # 부분집합 탐색
    for i in range(1 << 7):
        sub = []
        for j in range(7):
            if i & 1 << j:
                sub.append(j)
        Sub.append(sub)
    # 길이가 3인 부분집합만 추출 => 더하기!
    listS = []
    for i in Sub:
        if len(i) == 3 and Number[i[0]]+Number[i[1]]+Number[i[2]] not in listS:
            listS.append(Number[i[0]]+Number[i[1]]+Number[i[2]])
    # 내림차순으로 정렬
    listS.sort(reverse=True)
    print("#{} {}".format(TC, listS[4]))