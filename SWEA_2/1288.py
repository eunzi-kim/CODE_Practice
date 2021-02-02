T = int(input())

i = 0
for test_case in range(1, T+1):
    test_case = int(input())
    i += 1
    num_list = []
    n = 0
    case = str(test_case)
    while len(num_list) < 10:
        n += 1
        case = str(n * test_case)
        for x in case:  
            if x not in num_list:
                num_list.append(x)
            
    print(f'#{i} {case}')