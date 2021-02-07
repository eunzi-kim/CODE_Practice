a = int(input())
numbers = input()

for i in range(len(numbers)-1, -1, -1):
    result = int(numbers[i]) * a
    print(result)
print(a * int(numbers))