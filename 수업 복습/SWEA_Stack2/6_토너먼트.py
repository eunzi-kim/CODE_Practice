import sys
sys.stdin = open("4880_input.txt", "r")

# 선수 나누기
def game(start, end):
    if start == end:
        return start
    else:
        v1 = game(start, (start+end)//2)
        v2 = game((start+end)//2+1, end)
        # 경기장으로 보내기
        return battle(v1, v2)
# 카드 경기 하기(경기장)
def battle(x, y):
    # 1: 가위, 2: 바위, 3: 보
    # y가 이긴 경우 (= x가 진 경우)
    if (Card[x] == 1 and Card[y] == 2) or (Card[x] == 2 and Card[y] == 3) or (Card[x] == 3 and Card[y] == 1):
        return y
    # x가 이기거나 비긴 경우
    # 비긴 경우 => x가 y보다 앞 숫자이므로, x가 이긴 것으로 함
    else:
        return x

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    Card = list(map(int, input().split()))
    # 학생들 번호는 1부터, 인덱스는 0부터 시작이므로 1을 더해줌
    result = game(0, N-1) + 1
    print("#{} {}".format(TC, result))