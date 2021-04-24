def two(x, count):
    global result

    if count > 12:
        result = 'overflow'
        return
    if x == int(x):
        return
    else:
        result += str(int(x * 2))
        return two((x * 2) - (int(x * 2)), count+1)

T = int(input())
for TC in range(1, T+1):
    R = float(input())
    result = ''
    two(R, 0)
    print("#{} {}".format(TC, result))