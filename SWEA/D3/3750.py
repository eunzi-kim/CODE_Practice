# Digit sum

T = int(input())
# 결과 리스트
Result = []
for TC in range(T):
    Arr = list(input())
    # 한 자릿수가 될 때까지 반복
    while len(Arr) > 1:
        # 모든 자릿수의 합
        sumV = 0
        for i in range(len(Arr)):
            sumV += int(Arr[i])
        # 모든 자릿수의 합을 배열로 변경
        Arr = list(str(sumV))
    # 결과값
    Result.append(Arr[0])
# 결과값 출력
for TC in range(T):
    print("#{} {}".format(TC+1, Result[TC]))
