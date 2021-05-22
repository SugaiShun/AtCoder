import math
import sys
A,B,K = map(int,input().split())
MAX = A+B

cnt = 0
comb = 0

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def search(i,j,use,k,c):
    if i == A and j == B:
        print(use)
        sys.exit()
    elif i == A:
        search(i,j+1,use+'b',k,c)
    elif j == B:
        search(i+1,j,use+'a',k,c)
    else:
        if k <= c/2:
            search(i+1,j,use+'a',k-c/2,c/2)
        else:
            search(i,j+1,use+'b',k-c/2,c/2)

def main():
    global comb
    comb  = combinations_count(A+B,A)
    search(0,0,"",K,comb)

main()