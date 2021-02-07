a, b, c = map(int, input().split())

r1 = (a + b) % c
r2 = ((a % c) + (b % c)) % c
r3 = (a * b) % c
r4 = ((a % c) * (b % c)) % c

print(f'{r1}\n{r2}\n{r3}\n{r4}')