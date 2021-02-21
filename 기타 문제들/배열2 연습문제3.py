# 연습문제 복습

# 리스트 초기화
Arr = [[0 for _ in range(5)] for _ in range(5) ]

# 우 하 좌 상
dc = [0, 1, 0, -1]
dr = [1, 0, -1, 0]

# 달팽이 숫자 만들기
# 방향키 인덱스 초기화
i = 0
# 배열 인덱스 초기화
c = r = 0
# 배열에 1부터 25까지 숫자 넣기
for x in range(1, 26):
    Arr[c][r] = x

    while x < 25:
        # 직진했을때, 막히는 벽이 없는 경우
        if 0 <= c+dc[i] < 5 and 0 <= r+dr[i] < 5 and Arr[c+dc[i]][r+dr[i]] == 0:
            c += dc[i]
            r += dr[i]
            break
        # 직진했을때, 막히는 벽이 있는 경우
        # 방향키가 규칙적으로 반복된다.
        else:
            if i == 3:
                i = 0
            else:
                i += 1

# 리스트를 문자열로 변환
result = ''
for arr in Arr:
    for a in arr:
        result += str(a) + " "
    result += "\n"

print(result)