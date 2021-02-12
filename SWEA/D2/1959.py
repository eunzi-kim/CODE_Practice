# 두 개의 숫자열
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    # N = len(Ai) / M = len(Bj)
    # Ai : 0 1 2 / 0 1 2 / 0 1 2
    # Bj : 0 1 2 / 1 2 3 / 2 3 4