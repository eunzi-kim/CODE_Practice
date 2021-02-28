# 가랏! RC카!

import sys
sys.stdin = open("input.txt", "r")
# 중요포인트 : 속도의 값이 음수일때, 속도는 0이다!
T = int(input())
for TC in range(1, T+1):
    N = int(input())
    # 속도, 거리 초기화
    speed = 0
    distance = 0
    for n in range(N):
        Command = list(map(int, input().split()))
        # 가속
        if Command[0] == 1:
            speed += Command[1]
        # 감속
        elif Command[0] == 2:
            if speed < Command[0]:
                speed = 0
            else:
                speed -= Command[1]
        # 현재 속도 유지
        else:
            speed = speed
        # 거리에 속도 더하기
        distance += speed
    print("#{} {}".format(TC, distance))