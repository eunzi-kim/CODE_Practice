# 거듭 제곱
import sys
sys.stdin = open("input.txt", "r")

def cal (n, m):
    if m == 1:
        return n
    else:
        return cal(n, m-1) * n

for TC in range(1, 11):
    T = int(input())
    N, M = map(int, input().split())

    print("#{} {}".format(TC, cal(N, M)))
