# 짱 겨루기
def zzang(a, b):
    A = search_zzang(a)
    B = search_zzang(b)
    if A < B:
        Zzang[B] = A
        Zzang[b] = A
    else:
        Zzang[A] = B
        Zzang[a] = B
# 최강 짱 탐색
def search_zzang(x):
    if x == Zzang[x]:
        return x
    else:
        return search_zzang(Zzang[x])

T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    People = list(map(int, input().split()))
    # 짱 리스트
    Zzang = [x for x in range(N+1)]
    for i in range(M):
        p = People[2*i]
        q = People[2*i+1]
        zzang(p, q)
    # 진짜 짱 탐색
    Result = []
    for i in range(1, N+1):
        if search_zzang(Zzang[i]) not in Result:
            Result.append(search_zzang(Zzang[i]))
    print("#{} {}".format(TC, len(Result)))
