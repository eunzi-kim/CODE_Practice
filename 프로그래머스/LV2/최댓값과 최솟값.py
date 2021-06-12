def solution(s):
    maxV = -100000000000000
    minV = 1000000000000000
    a = ''
    for i in range(len(s)):
        if s[i] == " ":
            if int(a) > maxV:
                maxV = int(a)
            if int(a) < minV:
                minV = int(a)
            a = ''
        elif i == len(s)-1:
            a += s[i]
            if int(a) > maxV:
                maxV = int(a)
            if int(a) < minV:
                minV = int(a)
        else:
            a += s[i]
    answer = str(minV) + " " + str(maxV)
    return answer