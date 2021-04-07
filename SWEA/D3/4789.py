# 성공적인 공연 기획

T = int(input())
for TC in range(1, T+1):
    Person = list(map(int, input()))
    # 누적 박수 고객수
    clap = 0
    # 고용해야할 고객수
    hire = 0
    for i in range(len(Person)):
        clap += Person[i]
        if clap <= i:
            hire += 1
            clap += 1
    print("#{} {}".format(TC, hire))