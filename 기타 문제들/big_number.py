# 첫째 줄 N, M, K / K <= M
# 둘째 줄 N개의 자연수
# 동빈이의 큰 수의 법칙에 따라 더해진 답 출력

n, m, k = map(int, input().split())

num_list = list(map(int, input().split()))

sort_list = sorted(num_list)

if sort_list[n-1] == sort_list[n-2]:
    result = sort_list[n-1] * m
else:
    q = m // (k + 1)
    r = m % (k + 1)
    cycle = (sort_list[n-1] * k) + sort_list[n-2]
    result = cycle * q + r

print(result)