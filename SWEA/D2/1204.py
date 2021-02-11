# 최빈수 구하기

# 학생수 : 1000명, 최빈수 여러개 => 가장 큰 점수 출력

import sys
sys.stdin = open('1204.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    TC = int(input())
    scores = list(map(int, input().split()))

    number = [0] * 101
    for score in scores:
        number[score] += 1

    m_num = number[0]
    result = 0
    for i in range(101):
        if number[i] >= m_num:
            m_num = number[i]
            result = i  

    print(f'#{tc} {result}')