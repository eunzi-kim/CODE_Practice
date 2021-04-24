def game(Arr, j):
    # triplet 확인
    if Arr[j] >= 3:
        return 1
    # run 확인
    if 0 <= j < 8 and Arr[j] and Arr[j+1] and Arr[j+2]:
        return 1
    if 0 < j < 9 and Arr[j-1] and Arr[j] and Arr[j+1]:
        return 1
    if 1 < j < 10 and Arr[j-2] and Arr[j-1] and Arr[j]:
        return 1

T = int(input())
for TC in range(1, T+1):
    Card = list(map(int, input().split()))
    # 각자가 받을 카드 초기화
    A = [0] * 10
    B = [0] * 10
    result = 0
    for i in range(12):
        if i % 2 == 0:
            A[Card[i]] += 1
        else:
            B[Card[i]] += 1
        if game(A, Card[i]):
            result = 1
            break
        if game(B, Card[i]):
            result = 2
            break
    print("#{} {}".format(TC, result))