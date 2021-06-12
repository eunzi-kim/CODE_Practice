def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        subA = []
        for j in range(len(arr2[0])):
            subV = 0
            for k in range(len(arr1[0])):
                subV += arr1[i][k]*arr2[k][j]
            subA.append(subV)
        answer.append(subA)
    return answer