result = '*+++++'*4 + '*'
while len(result) >= 5:
    if len(result) == 5:
        print(result)
        result = ''
    else:
        print(result[0:5])
        result = result[5:len(result)+1]

