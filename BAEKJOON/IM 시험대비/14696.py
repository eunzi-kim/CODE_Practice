# 딱지놀이

T = int(input())
for tc in range(T):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 도형의 개수 카운트
    starA = cirA = squA = triA = 0
    for i in range(1, A[0]+1):
        if A[i] == 4:
            starA += 1
        elif A[i] == 3:
            cirA += 1
        elif A[i] == 2:
            squA += 1
        else:
            triA += 1

    starB = cirB = squB = triB = 0
    for j in range(1, B[0]+1):
        if B[j] == 4:
            starB += 1
        elif B[j] == 3:
            cirB += 1
        elif B[j] == 2:
            squB += 1
        else:
            triB += 1

    # 도형의 개수 비교
    if starA > starB:
        result = "A"
    elif starA < starB:
        result = "B"
    else:
        if cirA > cirB:
            result = "A"
        elif cirA < cirB:
            result = "B"
        else:
            if squA > squB:
                result = "A"
            elif squA < squB:
                result = "B"
            else:
                if triA > triB:
                    result = "A"
                elif triA < triB:
                    result = "B"
                else:
                    result = "D"

    print(result)