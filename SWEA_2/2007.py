T = int(input())

count = 0
for test_case in range(1, T+1):
    test_case = input()
    count += 1

    words = ''
    for idx in range(len(test_case)):
        words += test_case[idx]
        
        if test_case[idx+1:idx+1+len(words)] in words:
            break

    print(f'#{count} {idx+1}')