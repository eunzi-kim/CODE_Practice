T = input()

apb = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
idx = ''

for letter in T:
    idx += str(apb.index(letter)+1) + ' '
print(idx)

