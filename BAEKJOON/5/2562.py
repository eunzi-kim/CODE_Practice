# 최댓값

n_list = [0] * 9
for tc in range(9):
    n_list[tc] += int(input())

max_v = n_list[0]
max_i = 0
for i in range(9):
    if max_v <= n_list[i]:
        max_v = n_list[i]
        max_i = i+1

print(f'{max_v}\n{max_i}')