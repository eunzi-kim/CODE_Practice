import sys
sys.stdin = open("4881_input.txt", "r")

# 핵심 포인트: 순열 이용하기!
def perm(idx, midV):
    global minV
    # 중간합이 최소합 이상이면 X
    if midV > minV:
        return
    # 최소합 구하기
    if idx == N:
        if midV < minV:
            minV = midV
    else:
        for i in range(N):
            if not Visited[i]:
                Sel[idx] = i
                # 사용 기록 입력
                Visited[i] = True
                # 재귀를 이용한 순열
                # 중간합 더하기
                perm(idx+1, midV + Board[idx][i])
                # 다음 반복문을 위한 기록 원상복귀
                Visited[i] = False

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    Board = [list(map(int, input().split())) for _ in range(N)]
    # 순열 인덱스 리스트 초기화
    Sel = [0] * N
    # 사용 기록 리스트 초기화
    Visited = [False] * N
    # 최소값 초기화
    minV = 501
    perm(0, 0)
    print("#{} {}".format(TC, minV))
