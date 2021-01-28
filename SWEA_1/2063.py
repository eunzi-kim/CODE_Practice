T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
list_numbers = list(map(int, input().split()))
for idx in range(len(list_numbers)):
    if len(list_numbers) // 2  == idx:
        print(sorted(list_numbers)[idx])