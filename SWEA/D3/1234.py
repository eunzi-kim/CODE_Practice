# 비밀번호

for TC in range(1, 11):
    N, string = input().split()
    String = list(string)
    Stack = []
    i = 0
    while i < len(String)-1:
        if String[i] == String[i+1]:
            String.pop(i+1)
            String.pop(i)
            i = 0
        else:
            i += 1
    result = ''.join(String)
    print("#{} {}".format(TC, result))