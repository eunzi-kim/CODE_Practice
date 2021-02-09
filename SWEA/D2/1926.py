T = int(input())

list_369 = ['3', '6', '9']
for number in range(1, T+1):
    result = ''
    nums = 0
    for num in str(number):

        if num in list_369:
            nums += 1
            result = '-' * nums

        else:
            if nums >= 1:
                result = '-' * nums
            else:
                result = str(number)

    print(result, end=" ")