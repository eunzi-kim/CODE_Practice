# 문자열의 거울상

T = int(input())
for TC in range(1, T+1):
    String = input()
    mirror = []
    for i in range(len(String)-1, -1, -1):
        if String[i] == "p":
            mirror.append("q")
        elif String[i] == "q":
            mirror.append("p")
        elif String[i] == "b":
            mirror.append("d")
        else:
            mirror.append("b")
    result = "".join(mirror)
    print("#{} {}".format(TC, result))