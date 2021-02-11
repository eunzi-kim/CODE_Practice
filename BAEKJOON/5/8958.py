# OX퀴즈

T = int(input())
for tc in range(T):
    ox = input()
    
    result = 0
    count = 0
    for letter in ox:
        if letter == 'O':
            count += 1
        else:
            count = 0

        result += count

    print(result)