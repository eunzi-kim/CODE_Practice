# 어디에 단어가 들어갈 수 있을까

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num_list = []
    for n in range(N):
        num_list += list(map(int, input().split()))

    count = 0
    # 가로
    for a in range(0, len(num_list), N):
        r_count = 0
        for i in range(a, a+N):
            if num_list[i] == 1:
                r_count += 1
            else:
                r_count = 0

            if r_count == K:
                count += 1
            elif r_count == K+1:
                count -= 1

    # 세로
    for b in range(0, N):
        c_count = 0
        for j in range(b, N**2, N):
            if num_list[j] == 1:
                c_count += 1
            else:
                c_count = 0

            if c_count == K:
                count += 1
            elif c_count == K+1:
                count -= 1

    print(f'#{tc} {count}')
