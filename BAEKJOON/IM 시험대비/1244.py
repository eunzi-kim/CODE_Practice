# 스위치 켜고 끄기

N = int(input()) # 스위치 개수
Switch = list(map(int, input().split())) # 스위치 상태
M = int(input()) # 학생수

S = Switch
for m in range(M):
    G, number = map(int, input().split()) # 성별, 스위치 번호

    # 남자일 때, 스위치 상태 변경
    if G == 1:
        x = 1
        # 스위치 번호의 배수를 변경
        while number * x - 1 < N:
            if Switch[number * x - 1] == 1:
                Switch[number * x - 1] = 0
            else:
                Switch[number * x - 1] = 1
            x += 1

    # 여자일 때, 스위치 상태 변경
    else:
        i = number - 1
        j = 0
        # 스위치 번호를 중심으로 바깥으로 뻗어나가며 비교
        while j <= i < N - j and Switch[i - j] == Switch[i + j]:
            j += 1

        for k in range(j):
            if Switch[i - k] == 1:
                Switch[i - k] = 0
                Switch[i + k] = 0
            else:
                Switch[i - k] = 1
                Switch[i + k] = 1

# 리스트형을 20개씩 나눠서 문자열로 변환
for i in range(0, len(Switch), 20):
    print(*Switch[i:i+20])