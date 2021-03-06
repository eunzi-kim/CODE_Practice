# String

for TC in range(1, 11):
    T = int(input())
    Word = input()
    String = input()
    count = 0
    # 찾는 문자열 첫 글자
    for i in range(len(String)-len(Word)+1):
        letter = ""
        # 문자열 탐색
        for j in range(i, i+len(Word)):
            letter += String[j]
        if letter == Word:
            count += 1
    print("#{} {}".format(TC, count))