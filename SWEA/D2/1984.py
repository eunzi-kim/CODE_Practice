# 중간 평균값 구하기

T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split('')))

    for a in range(9, 0, -1):
        for i in range(a-1, -1, -1):
            if numbers[a] < numbers[i]:
                numbers[i], numbers[a] = numbers[a], numbers[i] 
    
    sum = 0
    for idx in range(1, 9):
        sum += numbers[idx]

    # 반올림 중요!
    result = round(sum / 8)

    print(numbers)
    print(f'#{tc} {result}')