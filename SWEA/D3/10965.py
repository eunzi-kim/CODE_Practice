# 제곱수 만들기

# 소수 만들기
Prime = [2]
for x in range(3, int(10000000**(0.5)), 2):
    for p in Prime:
        if x % p == 0:
            break
    else:
        Prime.append(x)
Answer = []
T = int(input())
for TC in range(1, T+1):
    A = int(input())
    result = 1
    if A ** 0.5 != int(A ** (0.5)):
        for p in Prime:
            count = 0
            while A % p == 0:
                count += 1
                A //= p
            if count % 2:
                result *= p
            if A == 1 or A < p:
                break
        if A > 1:
            result *= A
    Answer.append("#{} {}".format(TC, result))
for a in Answer:
    print(a)