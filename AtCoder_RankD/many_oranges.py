import math

A,B,W = map(int,input().split())

min_n = math.ceil(W*1000/B)
max_n = int(W*1000/A)
if (max_n - min_n) < 0:
    print("UNSATISFIABLE")
else:
    print(str(min_n)+" "+str(max_n))
