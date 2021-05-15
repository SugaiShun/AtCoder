def main():
    A = list(map(int,input().split()))

    A_sort = sorted(A)
    dif = 0
    for i in range(1,len(A)):
        a = A_sort[i-1]
        b = A_sort[i]
        if i == 1:
            dif = b - a
        else:
            if dif == (b-a):
                dif = b - a
            else:
                print("No")
                return 0

    print("Yes")

main()