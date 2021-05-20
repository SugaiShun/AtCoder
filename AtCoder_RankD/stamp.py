import math

def main():
    N,M = map(int,input().split())

    if M ==0:
        print(1)
        return 0

    A = list(map(int,input().split()))
    A.sort()

    B = []
    mini_k = 1000000001

    if M==N:
        print(0)
        return 0
    else:
        M +=1
    

    for i in range(M):
        if i == 0 and A[i]!=1:
            w = A[i]
        elif i == (M-1):
            w = N - A[i-1] + 1
        else:
            w = A[i] - A[i-1]
        
        if w>1:
            B.append(w-1)

        if mini_k > (w-1) and w>1:
            mini_k = w -1

    cnt=0
    for i in range(len(B)):
        cnt+=math.ceil((B[i])/mini_k)

    print(cnt)

main()
