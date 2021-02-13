# 파스칼의 삼각형

T = int(input())
for tc in range(1, T+1):
    t = int(input())

    result = ''
    N = [0] * t
    M = [0] * t
    for i in range(1, t+1):        
        for j in range(i):
            if j == 0 or j == i-1:
                N[j] = 1
            elif j < i // 2  + 1:
                N[j] = M[j] + M[j-1]
            else:
                N[j] = N[i-j-1]
        M = N[::]

        tri = ''
        for x in N:
            if x != 0:
                tri += str(x) + " "

        result += "\n" + tri
    print(f'#{tc}{result}')