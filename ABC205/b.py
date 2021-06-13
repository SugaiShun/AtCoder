def main():
    N = int(input())
    Nl = list(range(1,N+1))
    A = list(map(int,input().split()))

    for a in A:
        if a in Nl:
            Nl.remove(a)
        else:
            print("No")
            return 0

    print("Yes")


if __name__=="__main__":
    main()