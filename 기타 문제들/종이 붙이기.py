# 0223 복습

# 점화식: f(x) = f(x-1) + 2 * f(x-2)
def paper(M):
    if M == 10:
        return 1
    elif M == 20:
        return 3
    else:
        return paper(M - 10) + 2 * paper(M - 20)

T = int(input())
for TC in range(1, T+1):
    N = int(input())

    print("#{} {}".format(TC, paper(N)))