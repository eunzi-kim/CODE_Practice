# 0216 복습
# Ladder1

import sys
sys.stdin = open('input.txt', 'r')

for TC in range(1, 11):
    T = int(input())
    L = [list(map(int, input().split())) for _ in range(100)]

    # 목표 : 결승점 2에서 시작하여 시작점 찾기
    # 결승점 탐색
    for d in range(100):
        if L[99][d] == 2:
            ed = d

    # 결승점에서 시작
    r = 99
    c = ed

    # 1순위 : 좌, 우 / 2순위 : 상
    # 좌, 우 계속 반복되면 안되므로
    # 번호를 붙인 move라는 변수에 조건 만들기
    move = 0
    while r > 0:
        if (move == 0 or move == 1) and 0 < c and L[r][c-1] == 1:
            c -= 1
            move = 1
        elif (move == 0 or move == 2) and c < 99 and L[r][c+1] == 1:
            c += 1
            move = 2
        else:
            r -= 1
            move = 0

    print(f'#{T} {c}')