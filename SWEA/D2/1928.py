# Base64 Decoder

import sys
sys.stdin = open("input.txt", "r")
ASCII = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
T = int(input())
for TC in range(1, T+1):
    String = input()
    result = ''
    # 문자 => ASCII 값
    code = []
    for s in String:
        for i in range(64):
            if s == ASCII[i]:
                code.append(i)
    # ASCII 값 => 이진법 (6비트)
    Two = []
    for x in code:
        two = [0] * 6
        cnt = 5
        while x > 0:
            two[cnt] = x % 2
            x //= 2
            cnt -= 1
        for t in two:
            Two.append(t)
    # 2진법 => 8비트
    for i in range(0, len(Two)-7, 8):
        Num = []
        for j in range(i, i+8):
            Num.append(Two[j])
            # 역 인덱스: (2*i+5)-j
        # 8비트 => 10진법
        number = 0
        for i in range(8):
            if Num[i] == 1:
                number += 2**(7-i)
        result += chr(number)
    print("#{} {}".format(TC, result))