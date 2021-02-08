T = int(input())

if T >= 90:
    result = "A"
elif T >= 80:
    result = "B"
elif T >= 70:
    result = "C"
elif T >= 60:
    result = "D"
else:
    result = "F"

print(result)