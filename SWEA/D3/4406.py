# 모음이 보이지 않는 사람
T = int(input())
for TC in range(1, T+1):
    String = input()
    # 모음: a, e, i, o, u
    result = ""
    for letter in String:
        if letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u':
            result += letter
    print("#{} {}".format(TC, result))