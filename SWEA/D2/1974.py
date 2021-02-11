# 스도쿠 검증

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    numbers = []
    for n in range(9):
        numbers += map(int, input().split())

    r_num = [1] * 9
    for i in range(81):
        r_num[numbers[i]-1] -= 1
        if i % 9 == 8:
            if r_num == [0] * 9:
                r_num = [1] * 9
            else:
                r_result = 0
                break
            
            r_result = 1
         
    for j in range(9):
        c_num = [1] * 9
        for x in numbers[j:j+73:9]:
            c_num[x-1] -= 1
    

        if c_num == [0] * 9:
            c_result = 1                
        else:
            c_result = 0
            break
        
    for a in range(0, 7, 3):
        for b in range(a, 61, 27):
            s_num = [1] * 9
            for c in range(b, b+19, 9):
                s_num[numbers[c]-1] -= 1
                s_num[numbers[c+1]-1] -= 1
                s_num[numbers[c+2]-1] -= 1

            if s_num == [0] * 9:
                s_result = 1                
            else:
                s_result = 0
                break

    if r_result == 1 and c_result == 1 and s_result == 1:
        result = 1
    else:
        result = 0
    
    print(f'#{tc} {result}')
