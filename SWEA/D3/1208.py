# Flatten
import sys
sys.stdin = open("input.txt", "r")

for TC in range(1, 11):
    N = int(input())
    Box = list(map(int, input().split()))

    for n in range(N+1):
        # 최대값, 최소값 초기화
        maxV = Box[0]
        minV = Box[0]
        # 가장 높은 상자와 가장 낮은 상자 구하기
        for x in Box:
            if x > maxV:
                maxV = x
            if x < minV:
                minV = x

        # 가장 높은 상자의 높이 -1
        for i in range(100):
            if Box[i] == maxV:
                Box[i] -= 1
                break

        # 가장 낮은 상자의 높이 +1
        for j in range(100):
            if Box[j] == minV:
                Box[j] += 1
                break

    print("#{} {}".format(TC, maxV-minV))