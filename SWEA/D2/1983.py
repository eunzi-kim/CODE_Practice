# 조교의 성적 매기기

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    S = [0] * N
    for s in range(N):
        mt, et, hw = map(int,input().split())
        sum_s = mt * 0.35 + et * 0.45 + hw * 0.2
        S[s] += sum_s
    # S = 학생들의 총점 리스트
    # S_rank = 학생들의 총점 정렬
    S_rank = S[::]
    for j in range(N-1):
        for i in range(j+1, N):
            if S_rank[j] < S_rank[i]:
                S_rank[j], S_rank[i] = S_rank[i], S_rank[j]
    
    # rank : 학생들의 번호별 순위
    rank = [0] * N
    for x in range(N):
        for y in range(N):
            if  S[x] == S_rank[y]:
                rank[x] += y
    
    Grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    result = Grade[int((rank[K-1] / N) * 10)]
    print(f'#{tc} {result}')