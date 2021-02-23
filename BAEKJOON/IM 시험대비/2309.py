# 일곱 난쟁이

# 난쟁이 리스트 초기화
Tall = []
# 난쟁이 리스트에 키 push
for p in range(9):
    Tall.append(int(input()))

# 목표: 전체 난쟁이 키의 합 - 100 = 가짜 난쟁이의 키의 합
# 전체 난쟁이 키의 합
total = 0
for t in Tall:
    total += t
# 가짜 난쟁이의 키의 합
fake = total - 100

# 가짜 난쟁이 두 명 탐색
for i in range(9):
    for j in range(i+1, 9):
        if Tall[i] + Tall[j] == fake:
            I = i
            J = j
            break
# 가짜 난쟁이 난쟁이 리스트에서 없애기
Tall.pop(J)
Tall.pop(I)
# 난쟁이들 오름차순으로 출력
for short in sorted(Tall):
    print(short)