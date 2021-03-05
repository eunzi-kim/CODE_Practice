# 5C3

def Comb(k, s):
    if k == r:
        print(sel)
    else:
        for i in range(s, n-r+k+1):
            sel[k] = i
            Comb(k+1, i+1)

n = 5
r = 3
sel = [-1] * r
Comb(0, 0)