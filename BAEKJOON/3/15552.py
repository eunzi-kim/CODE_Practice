# 빠른 A + B
# 시간 초과 뜸!! 
# => import sys / sys.stdin.readline() 사용하여 해결!

T = int(input())

for test_case in range(1, T+1):
    a, b = map(int, input().split())
    result = a + b
    
    print(result)

