T = int(input())

for test_case in range(1, T+1):
    a = int(input())

    x_list = []
    y_list = []
    text = ''

    for b in range(1, a+1):
        x, y = map(str, input().split())
    
        x_list.append(x)
        y_list.append(y)

    for idx in range(0, a):
        text += x_list[idx] * int(y_list[idx])
        
    result = ''
    for i in range(0, len(text), 10):
        result += "\n" + text[i:i+10]

    print(f'#{test_case} {result}')
        
        
        

        
        
        
        
        
    

