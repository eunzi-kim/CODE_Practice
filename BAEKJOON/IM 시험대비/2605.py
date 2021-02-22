# 줄 세우기

N = int(input())
Pick = list(map(int, input().split()))

# 줄 세우기 리스트 초기화
Stand = []

# 1번부터 뽑은 번호 살펴보며 줄세우기
n = 0
while n < N:
    # 0번을 뽑은 경우
    if Pick[n] == 0:
        Stand.append(n+1)
    # 0번이 아닌 다른 번호를 뽑은 경우
    else:
        Stand.insert(n-Pick[n], n+1)
    n += 1

# 리스트를 문자열로 변경
result = ""
for x in Stand:
    result += str(x) + " "

print(result)