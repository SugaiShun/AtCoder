def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))

    newB = [0]*100001
    for i in range(N):
        newB[B[C[i]-1]] += 1

    cnt = 0
    for i in range(N):
        cnt += newB[A[i]]
    
    print(cnt)
main()