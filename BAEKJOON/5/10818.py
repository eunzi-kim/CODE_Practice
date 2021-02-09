# 최소, 최대

T = int(input())
list_num = list(map(int, input().split()))

max_v = list_num[0]
min_v = list_num[0]
for number in list_num:
    if number > max_v:
        max_v = number
    if number < min_v:
        min_v = number
    
print(min_v, max_v)