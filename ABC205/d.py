
def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))

    rslt = [0]*Q
    K = [0]*Q
    for i in range(Q):
        K[i] = int(input())
    
    newK = sorted(K)

    cnt=0
    i=0
    rslt=[0]*Q
    for j in range(N):
        if A[j] <= (newK[i]+cnt):
            cnt+=1
        else:
            rslt[i]=(newK[i]+cnt)
            i+=1
            if i==Q:
                return 0
    
    print(K[i]+cnt)

if __name__=="__main__":
    main()