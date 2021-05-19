def comb(base,l):
    a = 1
    for i in range(l):
        a = a * (base-i)
    b = 1
    for i in range(l):
        b = b*(l-i)
    return a//b

L = int(input())
base = L-1
rslt = comb(base,11)

print(rslt)