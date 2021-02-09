T = int(input())

for number in range(1, T+1):
    if T % number == 0:
        print(number, end=' ')