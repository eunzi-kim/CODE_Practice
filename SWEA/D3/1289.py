# 원재의 메모리 복구하기

T = int(input())
for TC in range(1, T+1):
    Memory = list(map(int, input()))
    # 초기화 상태
    First = [0]*len(Memory)
    # 수가 변화하는 인덱스 => 스택에 추가
    Stack = []
    # 메모리의 시작이 1인 경우도 스택에 추가!
    if Memory[0] == 1:
        Stack.append(0)
    for i in range(0, len(Memory)-1):
        if Memory[i] != Memory[i+1]:
            Stack.append(i)
    # 카운트 초기화
    count = 0
    # 메모리와 초기화가 같아지는 경우 반복문 멈춤
    while Memory != First:
        v = Stack.pop(0)
        if Memory[v] == 1:
            if First[v] == 1:
                for j in range(v+1, len(Memory)):
                    First[j] = 0
            else:
                for j in range(v, len(Memory)):
                    First[j] = 1
        else:
            if First[v] == 1:
                for j in range(v, len(Memory)):
                    First[j] = 0
            else:
                for j in range(v+1, len(Memory)):
                    First[j] = 1
        Stack.append(v+1)
        count += 1
    print("#{} {}".format(TC, count))