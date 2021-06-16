Amap = [0]*100001

def main():

    N = int(input())
    A = list(map(int,input().split()))
    for i in range(N):
        Amap[A[i]] += 1

    sumA = sum(A)

    Q = int(input())
    for i in range(Q):
        b,c = map(int,input().split())
        tmp1 = Amap[b]
        Amap[b] = 0
        Amap[c] += tmp1

        diff = tmp1*c - tmp1*b
        sumA += diff

        print(sumA)


if __name__=="__main__":
    main()