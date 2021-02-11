import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
for TC in range(1, T+1):
    N = int(input())

    Ai = [0] * N
    Bi = [0] * N
    for n in range(1, N+1):
        a, b = list(map(int, input().split()))
        Ai[n-1] += a
        Bi[n-1] += b
    P = int(input())
    plst = [0] * P
    c= 0
    for p in range(P):
        plst[c] += int(input())
        c += 1

    r_list = [0] * P

    for n in range(1, N + 1):
        a = Ai[n-1]
        b = Bi[n-1]
        for x in range(a, b+1):
            r_list[x-1] += 1

    result = ''
    for j in plst:
        result += str(r_list[j-1]) + ' '

    print(f'#{TC} {result}')